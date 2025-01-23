class URLS:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

    REGISTER_USER_API_URL = f'{BASE_URL}/api/auth/register'
    DELETE_USER_API_URL = f'{BASE_URL}/api/auth/user'
    ORDERS_API_URL = f'{BASE_URL}/api/orders'
    LOGIN_PAGE_URL = f'{BASE_URL}/login'
    FORGOT_PASSWORD_PAGE_URL = f'{BASE_URL}/forgot-password'
    ORDER_FEED_PAGE_URL = f'{BASE_URL}/feed'


class OrderInfo:
    CORRECT_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
