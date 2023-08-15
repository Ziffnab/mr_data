import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, \
    QPushButton, QRadioButton, QTabWidget, QLineEdit, QGroupBox, QComboBox, QTreeView, QListWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("RA-MI Interface")
        self.setGeometry(100, 100, 1280, 720)  # Set window size to 1280 x 720

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        # Tabbed Column (Column 1)
        tab_widget = QTabWidget()
        tab_widget.setTabPosition(QTabWidget.West)  # Set tabs on the left side

        # Add tabs
        # Account Tab
        account_tab = QWidget()
        account_tab_layout = QVBoxLayout()

        # Account Settings Section
        account_settings_group = QGroupBox("Account Settings")
        account_settings_layout = QVBoxLayout()

        # Account Name Label and Input
        account_name_label = QLabel("Account Name:")
        account_name_input = QLineEdit()
        account_settings_layout.addWidget(account_name_label)
        account_settings_layout.addWidget(account_name_input)

        # Account Email Label and Input
        account_email_label = QLabel("Account Email:")
        account_email_input = QLineEdit()
        account_settings_layout.addWidget(account_email_label)
        account_settings_layout.addWidget(account_email_input)

        # Account Password Label and Input
        account_password_label = QLabel("Account Password:")
        account_password_input = QLineEdit()
        account_password_input.setEchoMode(QLineEdit.Password)  # Hide entered text
        account_settings_layout.addWidget(account_password_label)
        account_settings_layout.addWidget(account_password_input)

        account_settings_group.setLayout(account_settings_layout)

        # Link Google Account Button
        link_google_button = QPushButton("Link Google Account")
        account_tab_layout.addWidget(link_google_button)

        # Create Basic Account Button
        create_account_button = QPushButton("Create Basic Account")
        account_tab_layout.addWidget(create_account_button)

        # Add Account Settings Group to Account Tab Layout
        account_tab_layout.addWidget(account_settings_group)

        account_tab.setLayout(account_tab_layout)

        # Add Account Tab to Tab Widget
        tab_widget.addTab(account_tab, "Account")

        # Authentication Tab
        authentication_tab = QWidget()
        authentication_layout = QVBoxLayout()

        # Username Input
        username_label = QLabel("Username:")
        username_input = QLineEdit()
        authentication_layout.addWidget(username_label)
        authentication_layout.addWidget(username_input)

        # Password Input
        password_label = QLabel("Password:")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)  # Hide password input
        authentication_layout.addWidget(password_label)
        authentication_layout.addWidget(password_input)

        # Login Button
        login_button = QPushButton("Login")
        authentication_layout.addWidget(login_button)

        # Create Account Button
        create_account_button = QPushButton("Create Account")
        authentication_layout.addWidget(create_account_button)

        authentication_tab.setLayout(authentication_layout)
        tab_widget.addTab(authentication_tab, "Authentication")

        # Context Tab
        context_tab = QWidget()
        context_layout = QVBoxLayout()

        # Context Selection
        context_label = QLabel("Select Context:")
        context_combobox = QComboBox()
        context_combobox.addItem("General")
        context_combobox.addItem("Technical")
        context_combobox.addItem("Specific Project")
        context_layout.addWidget(context_label)
        context_layout.addWidget(context_combobox)

        # Load Context Button
        load_context_button = QPushButton("Load Context")
        context_layout.addWidget(load_context_button)

        # Save Context Button
        save_context_button = QPushButton("Save Context")
        context_layout.addWidget(save_context_button)

        # Clear Context Button
        clear_context_button = QPushButton("Clear Context")
        context_layout.addWidget(clear_context_button)

        context_tab.setLayout(context_layout)
        tab_widget.addTab(context_tab, "Context")

        # Social Media Tab
        social_media_tab = QWidget()
        social_media_layout = QVBoxLayout()

        # Social Media Accounts
        accounts_groupbox = QGroupBox("Social Media Accounts")
        accounts_layout = QVBoxLayout()

        # Twitter Account
        twitter_label = QLabel("Twitter:")
        twitter_edit = QLineEdit()
        accounts_layout.addWidget(twitter_label)
        accounts_layout.addWidget(twitter_edit)

        # Facebook Account
        facebook_label = QLabel("Facebook:")
        facebook_edit = QLineEdit()
        accounts_layout.addWidget(facebook_label)
        accounts_layout.addWidget(facebook_edit)

        # Instagram Account
        instagram_label = QLabel("Instagram:")
        instagram_edit = QLineEdit()
        accounts_layout.addWidget(instagram_label)
        accounts_layout.addWidget(instagram_edit)

        accounts_groupbox.setLayout(accounts_layout)
        social_media_layout.addWidget(accounts_groupbox)

        # Social Media Feed
        feed_groupbox = QGroupBox("Social Media Feed")
        feed_layout = QVBoxLayout()

        # Twitter Feed
        twitter_feed_label = QLabel("Twitter Feed:")
        twitter_feed_textedit = QTextEdit()
        feed_layout.addWidget(twitter_feed_label)
        feed_layout.addWidget(twitter_feed_textedit)

        # Facebook Feed
        facebook_feed_label = QLabel("Facebook Feed:")
        facebook_feed_textedit = QTextEdit()
        feed_layout.addWidget(facebook_feed_label)
        feed_layout.addWidget(facebook_feed_textedit)

        # Instagram Feed
        instagram_feed_label = QLabel("Instagram Feed:")
        instagram_feed_textedit = QTextEdit()
        feed_layout.addWidget(instagram_feed_label)
        feed_layout.addWidget(instagram_feed_textedit)

        feed_groupbox.setLayout(feed_layout)
        social_media_layout.addWidget(feed_groupbox)

        social_media_tab.setLayout(social_media_layout)
        tab_widget.addTab(social_media_tab, "Social Media")

        # Resources Tab
        resources_tab = QWidget()
        resources_layout = QVBoxLayout()

        # Ingested Files Container
        files_groupbox = QGroupBox("Ingested Files Container")
        files_layout = QVBoxLayout()

        # List of Ingested Files
        files_list = QListWidget()
        files_layout.addWidget(files_list)

        files_groupbox.setLayout(files_layout)
        resources_layout.addWidget(files_groupbox)

        # Local Files
        local_files_groupbox = QGroupBox("Local Files")
        local_files_layout = QVBoxLayout()

        # File Browser
        file_browser = QTreeView()
        local_files_layout.addWidget(file_browser)

        local_files_groupbox.setLayout(local_files_layout)
        resources_layout.addWidget(local_files_groupbox)

        # Network Services
        network_groupbox = QGroupBox("Network Services")
        network_layout = QVBoxLayout()

        # List of Network Services
        network_list = QListWidget()
        network_layout.addWidget(network_list)

        network_groupbox.setLayout(network_layout)
        resources_layout.addWidget(network_groupbox)

        resources_tab.setLayout(resources_layout)
        tab_widget.addTab(resources_tab, "Resources")

        # Monitoring Tab
        monitoring_tab = QWidget()
        monitoring_layout = QVBoxLayout()

        # Local Monitoring
        local_monitoring_groupbox = QGroupBox("Local Monitoring")
        local_monitoring_layout = QVBoxLayout()

        # List of Local Monitoring Services
        local_monitoring_list = QListWidget()
        local_monitoring_layout.addWidget(local_monitoring_list)

        local_monitoring_groupbox.setLayout(local_monitoring_layout)
        monitoring_layout.addWidget(local_monitoring_groupbox)

        # Network Monitoring
        network_monitoring_groupbox = QGroupBox("Network Monitoring")
        network_monitoring_layout = QVBoxLayout()

        # List of Network Monitoring Services
        network_monitoring_list = QListWidget()
        network_monitoring_layout.addWidget(network_monitoring_list)

        network_monitoring_groupbox.setLayout(network_monitoring_layout)
        monitoring_layout.addWidget(network_monitoring_groupbox)

        monitoring_tab.setLayout(monitoring_layout)
        tab_widget.addTab(monitoring_tab, "Monitoring")

        layout.addWidget(tab_widget)

        # Conversational I/O (Column 2)
        conversation_layout = QVBoxLayout()

        # Conversational Text Output
        conversation_output = QTextEdit()
        conversation_output.setReadOnly(True)
        conversation_layout.addWidget(conversation_output)

        # Conversational Text Input
        conversation_input = QTextEdit()
        conversation_input.setPlaceholderText("Enter your message...")
        conversation_layout.addWidget(conversation_input)

        # Microphone and Image Icons
        microphone_icon = QPushButton(QIcon("mic.png"), "")
        image_icon = QPushButton(QIcon("images.png"), "")

        icon_layout = QHBoxLayout()
        icon_layout.addWidget(microphone_icon)
        icon_layout.addWidget(image_icon)

        conversation_layout.addLayout(icon_layout)

        layout.addLayout(conversation_layout)

        # Code Collaboration Section (Column 3)
        collaboration_layout = QVBoxLayout()

        # Special Characters Section
        special_chars_input = QTextEdit()
        special_chars_input.setPlaceholderText("Insert special characters...")
        collaboration_layout.addWidget(special_chars_input)

        # Code Collaboration Input
        code_collab_input = QTextEdit()
        code_collab_input.setPlaceholderText("Insert code snippet or upload file...")
        collaboration_layout.addWidget(code_collab_input)

        # Run Button
        run_button = QPushButton("Run")
        collaboration_layout.addWidget(run_button)

        layout.addLayout(collaboration_layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






