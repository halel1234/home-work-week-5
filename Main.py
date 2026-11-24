from About import AboutWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class HeatTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Heat Transfer")

        self.left_slider = QSlider(Qt.Orientation.Vertical)
        self.left_slider.setRange(0, 200)
        self.left_slider.setValue(200)

        self.left_body = QLabel()
        self.left_body.setObjectName("leftBody")
        self.left_body.setFixedSize(100, 150)

        self.right_body = QLabel()
        self.right_body.setObjectName("rightBody")
        self.right_body.setFixedSize(100, 150)

        self.right_slider = QSlider(Qt.Orientation.Vertical)
        self.right_slider.setRange(0, 200)
        self.right_slider.setValue(0)

        self.left_temp_label = QLabel("Temperature:")
        self.left_temp_box = QDoubleSpinBox()
        self.left_temp_box.setReadOnly(True)
        self.left_temp_box.setRange(0, 200)
        self.left_temp_box.setSuffix(" °C")

        self.left_mass_label = QLabel("Mass:")
        self.left_mass_box = QDoubleSpinBox()
        self.left_mass_box.setRange(0.01, 1000)
        self.left_mass_box.setValue(10)
        self.left_mass_box.setSuffix(" kg")

        self.left_capacity_label = QLabel("Heat capacity:")
        self.left_capacity_box = QDoubleSpinBox()
        self.left_capacity_box.setRange(0.01, 10000)
        self.left_capacity_box.setValue(0.4)
        self.left_capacity_box.setSuffix(" J/kg°C")

        self.right_temp_label = QLabel("Temperature:")
        self.right_temp_box = QDoubleSpinBox()
        self.right_temp_box.setReadOnly(True)
        self.right_temp_box.setSuffix(" °C")

        self.right_mass_label = QLabel("Mass:")
        self.right_mass_box = QDoubleSpinBox()
        self.right_temp_box.setRange(0, 200)
        self.right_mass_box.setRange(0.01, 1000)
        self.right_mass_box.setValue(10)
        self.right_mass_box.setSuffix(" kg")

        self.right_capacity_label = QLabel("Heat capacity:")
        self.right_capacity_box = QDoubleSpinBox()
        self.right_capacity_box.setRange(0.01, 10000)
        self.right_capacity_box.setValue(0.4)
        self.right_capacity_box.setSuffix(" J/kg°C")

        self.conductivity_label = QLabel("Conductivity:")
        self.conductivity_box = QDoubleSpinBox()
        self.conductivity_box.setRange(0.01, 100)
        self.conductivity_box.setValue(1)
        self.conductivity_box.setSuffix(" J/s°C")

        self.connector = QLabel()
        self.connector.setObjectName("connector")
        self.connector.setFixedHeight(16)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.setCheckable(True)
        self.graphs_button = QPushButton("Graphs")
        self.about_button = QPushButton("About")

        left_body_layout = QHBoxLayout()
        left_body_layout.addWidget(self.left_slider)
        left_body_layout.addWidget(self.left_body)

        right_body_layout = QHBoxLayout()
        right_body_layout.addWidget(self.right_body)
        right_body_layout.addWidget(self.right_slider)

        left_form = QFormLayout()
        left_form.addRow(self.left_temp_label, self.left_temp_box)
        left_form.addRow(self.left_mass_label, self.left_mass_box)
        left_form.addRow(self.left_capacity_label, self.left_capacity_box)

        right_form = QFormLayout()
        right_form.addRow(self.right_temp_label, self.right_temp_box)
        right_form.addRow(self.right_mass_label, self.right_mass_box)
        right_form.addRow(self.right_capacity_label, self.right_capacity_box)

        left_layout = QVBoxLayout()
        left_layout.addLayout(left_body_layout)
        left_layout.addLayout(left_form)

        right_layout = QVBoxLayout()
        right_layout.addLayout(right_body_layout)
        right_layout.addLayout(right_form)

        self.middle_controls = QVBoxLayout()
        self.middle_controls.addWidget(self.conductivity_label)
        self.middle_controls.addWidget(self.conductivity_box)
        self.middle_controls.addStretch()
        self.middle_controls.addWidget(self.connector)
        self.middle_controls.addStretch()
        self.middle_controls.addWidget(self.start_stop_button)
        self.middle_controls.addWidget(self.graphs_button)
        self.middle_controls.addWidget(self.about_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(self.middle_controls)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        self.left_slider.valueChanged.connect(self.left_temperature_changed)
        self.right_slider.valueChanged.connect(self.right_temperature_changed)
        self.start_stop_button.toggled.connect(self.start_stop_button_method)
        self.graphs_button.clicked.connect(self.graphs_button_method)
        self.about_button.clicked.connect(self.about_button_method)

        with open("style.qss", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def left_temperature_changed(self, value):
        pass  # my code here

    def right_temperature_changed(self, value):
        pass  # my code here

    def start_stop_button_method(self, checked):
        pass  # my code here

    def graphs_button_method(self):
        pass  # my code here

    def about_button_method(self):
        self.about_window.show()

    def timer_method(self):
        pass  # my code here


if __name__ == "__main__":
    app = QApplication()
    window = HeatTransfer()
    window.show()
    app.exec()
