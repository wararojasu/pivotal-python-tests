from core.ui.pages.tab_page import TabPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage
from pivotal_tracker.ui.pages.project_view.project_main import ProjectMain
from pivotal_tracker.ui.pages.project_view.projects_all import ProjectAll
from pivotal_tracker.ui.pages.profile.profile_page import ProfilePage
from pivotal_tracker.ui.pages.pop_ups.project_creation_form import ProjectCreationForm

go_dashboard_button = '.headerLogo__image'
projects_dropdown_list = '.tc_projects_dropdown_link.tc_context_name'
header_name = '//span[text()="$(expected_name)"]'
header_privacy = '//span[text()="($(privacy))"]'
show_all_projects_button = '//span[text()="Show All Projects"]'
user_options_dropdown = 'button[aria-label="Profile Dropdown"]'
profile_details_button = 'a[href*="/profile"][class*="Dropdown"]'


class UserPage(TabPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "header_name": lambda value: self.validate_header_name(value),
            "header_privacy": lambda value: self.validate_header_privacy(value)
        }
        self._tabs = {
            "Dashboard": lambda: self.get_dashboard_tab(),
            "ProjectMain": lambda: self.get_project_main_tab(),
            "AllProjects": lambda: self.get_all_projects(),
            "ProjectCreation": lambda: self.get_project_creation_form(),
            "Profile": lambda: self.get_profile_tab()
        }
        self._tab = DashboardPage(self._driver)

    def get_dashboard_tab(self):
        self.click(go_dashboard_button)
        self._tab = DashboardPage(self._driver)

    def get_project_main_tab(self):
        self._tab = ProjectMain(self._driver)

    def get_all_projects(self):
        self.click(projects_dropdown_list)
        self.click(show_all_projects_button)
        self._tab = ProjectAll(self._driver)

    def get_project_creation_form(self):
        self._tab = ProjectCreationForm(self._driver)

    def get_profile_tab(self):
        self.click(user_options_dropdown)
        self.click(profile_details_button)
        self._tab = ProfilePage(self._driver)

    def validate_header_name(self, name):
        return self.is_existing(header_name.replace('$(expected_name)', name))

    def validate_header_privacy(self, privacy):
        return self.is_existing(header_privacy.replace('$(privacy)', privacy))
