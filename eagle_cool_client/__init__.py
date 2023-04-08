import json
import typing
import requests


class EagleCoolClient:
    def __init__(self):
        self.base_url = "http://localhost:41595"

    # /api/folder/rename
    def rename_folder(self, folder_id: str, new_name: str):
        url = f"{self.base_url}/api/folder/rename"
        headers = {"Content-Type": "application/json"}
        data = {"folderId": folder_id, "newName": new_name}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/folder/update
    def update_folder(
        self, folder_id: str, new_name: str, new_description: str, new_color: str
    ):
        url = f"{self.base_url}/api/folder/update"
        headers = {"Content-Type": "application/json"}
        data = {
            "folderId": folder_id,
            "newName": new_name,
            "newDescription": new_description,
            "newColor": new_color,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/folder/list
    def list_folders(self):
        url = f"{self.base_url}/api/folder/list"
        response = requests.get(url)
        return response.json()

    # /api/folder/listRecent
    def list_recent_folders(self):
        url = f"{self.base_url}/api/folder/listRecent"
        response = requests.get(url)
        return response.json()

    # /api/item/addFromURL
    def add_item_from_url(
        self,
        url: str,
        name: str,
        website: str,
        tags: list,
        modification_time: int,
        headers: dict,
    ):
        url = f"{self.base_url}/api/item/addFromURL"
        headers = {"Content-Type": "application/json"}
        data = {
            "url": url,
            "name": name,
            "website": website,
            "tags": tags,
            "modificationTime": modification_time,
            "headers": headers,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/addFromURLs
    def add_items_from_urls(self, items: list, folder_id: str):
        url = f"{self.base_url}/api/item/addFromURLs"
        headers = {"Content-Type": "application/json"}
        data = {"items": items, "folderId": folder_id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/addFromPath
    def add_item_from_path(
        self,
        path: str,
        name: str,
        website: str,
        tags: list,
        annotation: str,
        folder_id: str,
    ):
        url = f"{self.base_url}/api/item/addFromPath"
        headers = {"Content-Type": "application/json"}
        data = {
            "path": path,
            "name": name,
            "website": website,
            "tags": tags,
            "annotation": annotation,
            "folderId": folder_id,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/addFromPaths
    def add_items_from_paths(self, items: list, folder_id: str):
        url = f"{self.base_url}/api/item/addFromPaths"
        headers = {"Content-Type": "application/json"}
        data = {"items": items, "folderId": folder_id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/addBookmark
    def add_bookmark(self, url: str, name: str, tags: list, base64: str):
        url = f"{self.base_url}/api/item/addBookmark"
        headers = {"Content-Type": "application/json"}
        data = {"url": url, "name": name, "tags": tags, "base64": base64}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/info
    def get_item_info(self, id: str):
        url = f"{self.base_url}/api/item/info?id={id}"
        response = requests.get(url)
        return response.json()

    # /api/item/thumbnail
    def get_item_thumbnail(self, id: str):
        url = f"{self.base_url}/api/item/thumbnail?id={id}"
        response = requests.get(url)
        return response.json()

    # /api/item/list
    def list_items(
        self,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ext: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        folders: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ):
        ext_filter = f"&ext={ext}" if ext else ""
        name_filter = f"&name={name}" if name else ""
        folders_filter = f"&folders={folders}" if folders else ""
        tags_filter = f"&tags={tags}" if tags else ""
        limit_filter = f"&limit={limit}" if limit else ""
        order_by_filter = f"&order_by={order_by}" if order_by else ""
        url = f"{self.base_url}/api/item/list?{folders_filter}{order_by_filter}{limit_filter}{ext_filter}{name_filter}{tags_filter}"
        response = requests.get(url)
        return response.json()

    # /api/item/moveToTrash
    def move_items_to_trash(self, item_ids: list):
        url = f"{self.base_url}/api/item/moveToTrash"
        headers = {"Content-Type": "application/json"}
        data = {"itemIds": item_ids}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/refreshPalette
    def refresh_palette(self, id: str):
        url = f"{self.base_url}/api/item/refreshPalette"
        headers = {"Content-Type": "application/json"}
        data = {"id": id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/refreshThumbnail
    def refresh_thumbnail(self, id: str):
        url = f"{self.base_url}/api/item/refreshThumbnail"
        headers = {"Content-Type": "application/json"}
        data = {"id": id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/restoreFromTrash
    def restore_items_from_trash(self, item_ids: list):
        url = f"{self.base_url}/api/item/restoreFromTrash"
        headers = {"Content-Type": "application/json"}
        data = {"itemIds": item_ids}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    # /api/item/update
    def update_item(
        self,
        id: str,
        name: str|None = None,
        description: str|None = None,
        tags: list|None = None,
        annotation: str|None = None,
        star: str|None = None,
    ):
        url = f"{self.base_url}/api/item/update"
        headers = {"Content-Type": "application/json"}
        data = {
            "id": id,
            "url": url,
            "tags": tags,
            "annotation": annotation,
            "star": star,
        }
        new_data = {}
        for k, v in data.items():
            if v is not None:
                new_data[k] = data[k]
        response = requests.post(url, headers=headers, data=json.dumps(new_data))
        return response.json()

    # /api/library/list
    def get_library_list(self):
        url = f"{self.base_url}/library/list"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    # /api/library/history
    def get_library_history(self):
        url = f"{self.base_url}/library/history"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    # /api/library/switch
    def switch_library(self, library_path):
        url = f"{self.base_url}/library/switch"
        data = {"libraryPath": library_path}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        data = json.loads(response.text)
        return data
