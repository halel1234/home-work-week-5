from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("About Heat Transfer")
        self.setObjectName("aboutWindow")
        self.setFixedSize(440, 470)

        self.card = QFrame()
        self.card.setObjectName("aboutCard")

        self.profile_picture = QLabel()
        self.profile_picture.setObjectName("profilePicture")
        self.profile_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.profile_picture.setFixedSize(136, 136)

        picture = QPixmap("profile.jpg")
        if not picture.isNull():
            picture = picture.scaled(
                128,
                128,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation,
            )
            x_offset = (picture.width() - 128) // 2
            y_offset = (picture.height() - 128) // 2
            self.profile_picture.setPixmap(picture.copy(x_offset, y_offset, 128, 128))
        else:
            self.profile_picture.setText("HH")

        self.name_label = QLabel("Halel Harburger")
        self.name_label.setObjectName("aboutName")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.description_label = QLabel("Heat transfer simulation between two bodies")
        self.description_label.setObjectName("aboutDescription")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setWordWrap(True)

        self.email_label = QLabel("halelharburger@gmail.com")
        self.email_label.setObjectName("aboutEmail")
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.github_link = QLabel(
            '<a href="https://github.com/halel1234/home-work-week-5">View GitHub repository &#8599;</a>'
        )
        self.github_link.setObjectName("githubLink")
        self.github_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.github_link.setOpenExternalLinks(True)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(32, 30, 32, 30)
        card_layout.setSpacing(14)
        card_layout.addWidget(self.profile_picture, alignment=Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.name_label)
        card_layout.addWidget(self.description_label)
        card_layout.addWidget(self.email_label)
        card_layout.addSpacing(4)
        card_layout.addWidget(self.github_link)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(self.card)

        with open("style.qss", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())
