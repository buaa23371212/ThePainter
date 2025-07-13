# 必备库
import requests
from bs4 import BeautifulSoup
import json

# ========================================== 模拟登录示例 ========================================== #
SESSION = requests.Session()
LOGIN_URL = "http://localhost:8080/merchant/login"

def login(username, password):
    try:
        # 1. 访问登录页面获取初始Cookie
        login_page = SESSION.get(LOGIN_URL)
        login_page.raise_for_status()
        
        # 2. 提交登录表单
        form_data = {
            "username": username,
            "password": password
        }
        
        # 3. 发送登录请求
        response = SESSION.post(LOGIN_URL, data=form_data)
        response.raise_for_status()
        
        # 4. 验证登录结果
        if response.url != LOGIN_URL:
            print("登录成功！已重定向至:", response.url)
            return True
        
        # 处理登录失败情况
        soup = BeautifulSoup(response.text, 'html.parser')
        error_div = soup.find("div", {"class": "alert-warning"})
        
        if error_div and "用户名或密码错误" in error_div.text:
            print("登录失败：用户名或密码错误")
        else:
            print("登录失败：未知原因")
        
        return False
    
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {str(e)}")
        return False

# ========================================== 店铺信息模块 ========================================== #
def get_shop_info(session):
    """获取店铺信息"""
    try:
        # 获取商家工作台页面
        dashboard_url = "http://localhost:8080/merchant#shop"  # 直接访问店铺页面
        dashboard_page = session.get(dashboard_url)
        dashboard_page.raise_for_status()
        
        # 解析页面获取店铺信息
        soup = BeautifulSoup(dashboard_page.text, 'html.parser')
        
        # 查找店铺信息部分
        shop_section = soup.find('section', id='shop')
        if not shop_section:
            print("未找到店铺信息部分")
            return None
        
        # 提取店铺名
        shop_name_h2 = shop_section.find('h2')
        if not shop_name_h2:
            print("在店铺部分未找到店铺名")
            return None
        
        shop_name = shop_name_h2.text.split('-')[-1].strip()
        
        # 创建店铺信息字典
        shop_info = {
            "name": shop_name,
            "status": "未知",
            "reviews": 0,
            "products": 0
        }
        
        # 尝试提取其他信息（如果存在）
        # 状态管理信息
        status_tab = shop_section.find('a', href="#shop-status")
        if status_tab:
            # 这里可以添加更复杂的解析逻辑
            shop_info["status"] = "正常营业"  # 默认值
        
        # 评价管理信息
        reviews_tab = shop_section.find('a', href="#shop-reviews")
        if reviews_tab:
            # 这里可以添加解析评价数量的逻辑
            pass
        
        # 商品管理信息
        products_tab = shop_section.find('a', href="#shop-products")
        if products_tab:
            # 这里可以添加解析商品数量的逻辑
            pass
        
        return shop_info
    
    except requests.exceptions.RequestException as e:
        print(f"获取店铺信息失败: {str(e)}")
        return None

# ========================================== 主程序 ========================================== #
if __name__ == "__main__":
    # 测试登录
    if login("admin", "000000"):
        # 登录成功后获取店铺信息
        shop_info = get_shop_info(SESSION)
        if shop_info:
            print("\n店铺信息:")
            print(f"店铺名: {shop_info['name']}")
            print(f"状态: {shop_info['status']}")
            # 可以添加更多信息的输出
        else:
            print("未能获取店铺信息")