import pytest
from eagle_cool_client import EagleCoolClient

class TestEagleCoolClient:
    @pytest.fixture
    def client(self):
        return EagleCoolClient()

    def test_rename_folder(self, client):
        response = client.rename_folder("folder_id", "new_name")
        assert response["status"] == "success"

    def test_update_folder(self, client):
        response = client.update_folder("folder_id", "new_name", "new_description", "new_color")
        assert response["status"] == "success"

    def test_list_folders(self, client):
        response = client.list_folders()
        assert isinstance(response, list)

    def test_list_recent_folders(self, client):
        response = client.list_recent_folders()
        assert isinstance(response, list)

    def test_add_item_from_url(self, client):
        response = client.add_item_from_url("url", "name", "website", ["tag"], 123456, {"header": "value"})
        assert response["status"] == "success"

    def test_add_items_from_urls(self, client):
        response = client.add_items_from_urls([{"url": "url", "name": "name"}], "folder_id")
        assert response["status"] == "success"

    def test_add_item_from_path(self, client):
        response = client.add_item_from_path("path", "name", "website", ["tag"], "annotation", "folder_id")
        assert response["status"] == "success"

    def test_add_items_from_paths(self, client):
        response = client.add_items_from_paths([{"path": "path", "name": "name"}], "folder_id")
        assert response["status"] == "success"

    def test_add_bookmark(self, client):
        response = client.add_bookmark("url", "name", ["tag"], "base64")
        assert response["status"] == "success"

    def test_get_item_info(self, client):
        response = client.get_item_info("id")
        assert isinstance(response, dict)

    def test_get_item_thumbnail(self, client):
        response = client.get_item_thumbnail("id")
        assert isinstance(response, dict)

    def test_list_items(self, client):
        response = client.list_items("order_by", 10, "ext", "name", "folders", "tags")
        assert isinstance(response, list)

    def test_move_items_to_trash(self, client):
        response = client.move_items_to_trash(["item_id"])
        assert response["status"] == "success"

    def test_refresh_palette(self, client):
        response = client.refresh_palette("id")
        assert response["status"] == "success"

    def test_refresh_thumbnail(self, client):
        response = client.refresh_thumbnail("id")
        assert response["status"] == "success"

    def test_restore_items_from_trash(self, client):
        response = client.restore_items_from_trash(["item_id"])
        assert response["status"] == "success"

    def test_update_item(self, client):
        response = client.update_item("id", "new_name", "new_description", ["new_tag"], "new_folder_id", "new_annotation", "new_color")
        assert response["status"] == "success"

    def test_get_library_list(self, client):
        response = client.get_library_list()
        assert isinstance(response, list)

    def test_get_library_history(self, client):
        response = client.get_library_history()
        assert isinstance(response, list)

    def test_switch_library(self, client):
        response = client.switch_library("library_path")
        assert response["status"] == "success"