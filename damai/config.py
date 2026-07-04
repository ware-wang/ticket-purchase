# -*- coding: UTF-8 -*-
"""
__Author__ = "WECENG"
__Version__ = "1.0.0"
__Description__ = "配置类"
__Created__ = 2023/10/11 18:01
"""


class Config:

    def __init__(
        self,
        index_url,
        login_url,
        target_url,
        users,
        city,
        dates,
        prices,
        if_listen,
        if_commit_order,
        max_retries=1000,
        fast_mode=True,
        page_load_delay=2,
        pre_start_delay=5,
        refresh_interval=0.15,
        post_click_interval=0.1,
    ):
        self.index_url = index_url
        self.login_url = login_url
        self.target_url = target_url
        self.users = users
        self.city = city
        self.dates = dates
        self.prices = prices
        self.if_listen = if_listen
        self.if_commit_order = if_commit_order
        self.max_retries = max_retries
        self.fast_mode = fast_mode  # 快速模式：减少等待时间和调试输出
        self.page_load_delay = page_load_delay  # 订单确认页加载等待时间（秒）
        self.pre_start_delay = pre_start_delay  # 开始轮询前预留给人工确认的等待时间（秒）
        self.refresh_interval = refresh_interval  # 未开售时刷新间隔（秒）
        self.post_click_interval = post_click_interval  # 点击购票入口后的状态探测间隔（秒）
