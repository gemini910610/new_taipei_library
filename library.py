import requests
import json

# 新北市立圖書館
class Library:
    class Area:
        def __init__(self, data: dict):
            self.name: str = data['areaName']
            self.free: int = data['freeCount']
            self.total: int = data['totalCount']
            self.branch: str = data['branchName']
        
        def __str__(self) -> str:
            return f'{self.branch} {self.name} : {self.free}/{self.total}'

    IDs = {
        '板橋分館': 2100,
        '板橋江子翠分館': 2101,
        '板橋四維分館': 2103,
        '永和民權分館': 2120,
        '林口分館': 2123,
        '三重分館': 2124,
        '三重南區分館': 2129,
        '新莊中港分館': 2133,
        '新莊分館': 2134,
        '新莊聯合分館': 2136,
        '泰山分館': 2148,
        '樹林分館': 2152,
        '中和分館': 2161,
        '新店分館': 2162,
        '新店柴埕圖書閱覽室': 2172,
        '新店三民圖書閱覽室': 2176,
        '新北市青少年圖書館': 2177,
        '淡水分館': 2180,
        '新北市立圖書館總館': 2204,
        '三峽北大分館': 2205,
    }
    URL = 'https://seat.library.ntpc.gov.tw/sm/dwr/call/plaincall/InquireResourceController.getAreaStatusUpdate.dwr'
    POST_DATA = {
        'callCount': '1',
        'windowName': '',
        'c0-scriptName': 'InquireResourceController',
        'c0-methodName': 'getAreaStatusUpdate',
        'c0-id': '0',
        'c0-param2': 'number:30',  # count of item in one page
        'batchId': '0',
        'instanceId': '0',
        'page': '%2Fsm%2Fhome_web.do',
        'scriptSessionId': 'WONxcuX57nSVpeli8G6ocqWvTuo-2/QUbATuo-jLJb9FWR7',
    }

    def __init__(self):
        pass

    def get_areas(self, library_name: str | None = None) -> list:
        post_data = self.POST_DATA.copy()
        post_data['c0-param0'] = f'number:{-1 if library_name is None else self.IDs[library_name]}'
        page = 0
        areas = []
        while True:
            post_data['c0-param1'] = f'number:{page}'
            response = requests.post(self.URL, post_data)
            response = response.text
            response = response.splitlines()[5]
            l_index = response.index('{')
            r_index = response.rindex('}')
            response = response[l_index : r_index + 1].replace('\\"', '"')
            response = json.loads(response)
            for d in response['data']:
                areas.append(self.Area(d))
            page = page + 1
            if page == response['totalPageCount']:
                break
        return self.group_areas(areas)
    
    def group_areas(self, areas: list):
        area_group = {}
        for area in areas:
            branch = area.branch
            if branch not in area_group:
                area_group[branch] = []
            area_group[branch].append(area)
        return area_group

    def get_libraries(self) -> list[str]:
        return list(self.IDs.keys())


# library = Library()
# libraries = library.get_libraries()
# areas = library.get_areas('新北市立圖書館總館')
# for area in areas:
#     print(area)
