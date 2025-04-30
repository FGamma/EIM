from PySide6.QtGui import QImageReader, QImageWriter


def load_image(fileName):
    reader = QImageReader(fileName)
    reader.setAutoTransform(True)
    new_image = reader.read()
    if new_image.isNull():
        return None, reader.errorString()
    return new_image, None


def save_image(image, fileName):
    writer = QImageWriter(fileName)
    if not writer.write(image):
        return False, writer.errorString()
    return True, None
