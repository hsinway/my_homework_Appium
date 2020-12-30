from ent_Wechat_PO_20201227_Sun.page.app_initial import App


class TestWechat:
    def setup(self):
        self.app_ini = App()
        self.app_ini.start()

    def teardown(self):
        self.app_ini.quit()

    def test_add_member(self):
        result = self.app_ini.goto_main().goto_address().click_add_member().add_member_manual().add_contact()
        assert "添加成功" in result

    def test_delete_member(self):
        result = self.app_ini.goto_main().goto_address().click_member().delete_member()
        assert "user9" not in result
