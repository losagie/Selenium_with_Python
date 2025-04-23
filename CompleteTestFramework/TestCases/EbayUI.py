import time
import pytest
import webdriver_manager
from ddt import unpack
from scripts.run_emscripten_tests import driver

from Base.test_Basedriver import BaseDriver
from Pages.test_ChoiceitemPage import ChooseItem
from Pages.test_EbayLaunchPage import Search_Item
from Utilities.Utillity import Utils
from ddt import ddt, data,unpack


@pytest.mark.usefixtures('setup_meth')
@ddt
class Test_EbayWebsite():

    #@data(*Utils.read_from_excel("C:\\Users\\HP\\PycharmProjects\\CompleteTestFramework\\Testdata\\ebaytest1.xlsx","Sheet1"))
    def __init__(self):
        self.driver = driver

    @data(*Utils.read_from_excel("../Testdata/ebaytest.xlsx","Sheet1"))
    @unpack
    def test_ebay_website(self,chosen,cindex,windex):
        SI = Search_Item(self.driver)
        SI.search_items(self)
        SI.search_clicks()
        SI.remove_text1()
        CI = ChooseItem(self.driver)
        CI.choice_item_scroll()
        ut = Utils(self.driver)
        ut.window_tabs()
        SI.choose_categories(self)
        ut.window_list(self)






