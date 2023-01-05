import pytz
import datetime
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsDropShadowEffect

app = QApplication([])  # Create a QApplication instance
label = QLabel("")  # Create a QLabel to display the time remaining

# Set the font size and weight
label.setStyleSheet("QLabel { font-size: 20pt; font-weight: bold; color: white; }")

# Set the width and height
label.setFixedWidth(300)
label.setFixedHeight(125)

# Set the background color
label.setAutoFillBackground(True)
palette = label.palette()
palette.setColor(label.backgroundRole(), QColor(0, 0, 0))  # Soothing blue
label.setPalette(palette)

# Add a drop shadow effect to the label
effect = QGraphicsDropShadowEffect()
effect.setBlurRadius(8)
effect.setOffset(2, 2)
label.setGraphicsEffect(effect)

def update_time():
    """Update the time remaining on the label"""
    """List on the this repo - https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568"""
    
    monterrey_tz = pytz.timezone('America/Monterrey')  # Monterrey time zone
    current_time_for_monterrey = datetime.datetime.now(monterrey_tz)  # Get the current time for Monterrey
    end_of_day_for_monterrey = datetime.datetime.now(monterrey_tz).replace(hour=23, minute=59, second=59)#, microsecond=999999)  # End of day for Monterrey
    time_remaining_for_monterrey = end_of_day_for_monterrey - current_time_for_monterrey  # Calculate the time remaining for Monterrey
    
    india_tz = pytz.timezone('Asia/Kolkata')  # India time zone
    current_time_for_india = datetime.datetime.now(india_tz)  # Get the current time for India
    end_of_day_for_india = datetime.datetime.now(india_tz).replace(hour=23, minute=59, second=59)#, microsecond=999999)  # End of day for India
    time_remaining_for_india = end_of_day_for_india - current_time_for_india  # Calculate the time remaining for Monterrey
    
    label.setWordWrap(True)
    return label.setText(str("India : ")+str(time_remaining_for_india)+str("\n")+str("Monterrey : ")+str(time_remaining_for_monterrey))  # Set the time remaining on the label

update_time()  # Initialize the time
label.show()  # Show the label

# Update the time every second
timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)  # 1 second in milliseconds

app.exec_()  # Run the event loop