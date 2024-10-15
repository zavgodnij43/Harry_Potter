# Оформлення
QSS = '''

/* Стиль для QPushButton */
QPushButton {
    background-color: #3B3A30;  /* Темный цвет для кнопок */
    color: #E3D5B3;  /* Цвет бумаги или пергамента */
    font: bold 14px "Lumos";  /* Специальный шрифт в стиле магии */
    padding: 10px;
    border-radius: 10px;
    border: 2px solid #7C3F00;  /* Цвет золота или меди */
}

QPushButton:hover {
    background-color: #5C4A33;  /* Темный оттенок при наведении */
}

QPushButton:pressed {
    background-color: #2E261B;
    border-style: inset;
}

/* Стиль для QLabel */
QLabel {
    font: 18px "Harry P";  /* Тематический шрифт */
    color: #000;  /* Золотистый цвет */
    padding: 5px;
    background-color: transparent;
}

/* Стиль для QGroupBox */
QGroupBox {
    border: 2px solid #7C3F00;  /* Золотистая граница */
    border-radius: 5px;
    margin-top: 10px;
    font: bold 12px "Lumos";
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}

/* Стиль для QRadioButton */
QRadioButton {
    font: 16px "Harry P";
    color: #643517;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
    border-radius: 8px;
    border: 2px solid #7C3F00;
    background-color: #3B3A30;
}

QRadioButton::indicator:checked {
    background-color: #FFD700;
}

/* Стиль для QSpinBox */
QSpinBox {
    border: 2px solid #7C3F00;
    padding: 5px;
    font: 12px "Lumos";
    background-color: #3B3A30;
    color: #E3D5B3;
}

/* Фон для основного окна */
QWidget#mainWindow,QWidget#cardWindow {
    background-image: url("wp10438846");  /* Изображение Хогвартса */
    background-repeat: no-repeat;
    background-position: center;
    background-color: #1C1C1C;  /* Темный фон, если изображение не загрузится */
}

QWidget {
    font: 20px "Lumos";  /* Общий шрифт */
    /*color: #E3D5B3;*/
}

'''

