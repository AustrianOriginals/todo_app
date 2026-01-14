import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QTextEdit, QComboBox, QDateEdit, QPushButton, QListWidget,
                             QListWidgetItem, QLabel, QCheckBox, QMessageBox, QFrame, QScrollArea, QMenu)
from PyQt6.QtCore import Qt, QDate, QSize, QPropertyAnimation, QEasingCurve, pyqtSignal, QTimer
from PyQt6.QtGui import QColor, QFont, QIcon, QPixmap
from pathlib import Path


class Task:
    """Task data model"""
    def __init__(self, title, description="", priority="Medium", due_date=None, task_id=None):
        self.id = task_id or str(datetime.now().timestamp())
        self.title = title
        self.description = description
        self.priority = priority  # High, Medium, Low
        self.due_date = due_date
        self.completed = False
        
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed
        }
    
    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['priority'], data['due_date'], data['id'])
        task.completed = data.get('completed', False)
        return task


class TaskManager:
    """Manage task persistence"""
    def __init__(self):
        self.data_file = Path.home() / '.todoapp' / 'tasks.json'
        self.data_file.parent.mkdir(exist_ok=True)
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data]
            except:
                self.tasks = []
        
    def save_tasks(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
    
    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
    
    def get_sorted_tasks(self, sort_by='priority'):
        """Sort tasks by priority, due_date, or name"""
        if sort_by == 'priority':
            priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
            return sorted(self.tasks, key=lambda t: (t.completed, priority_order.get(t.priority, 3)))
        elif sort_by == 'due_date':
            return sorted(self.tasks, key=lambda t: (t.completed, t.due_date or '9999-12-31'))
        else:  # name
            return sorted(self.tasks, key=lambda t: (t.completed, t.title.lower()))


class ThemeManager:
    """Manage light and dark themes"""
    DARK_RED = "#8B1538"
    LIGHT_ACCENT = "#E8B4BA"
    DARK_BG = "#1E1E1E"
    LIGHT_BG = "#FFFFFF"
    DARK_TEXT = "#FFFFFF"
    LIGHT_TEXT = "#000000"
    
    @staticmethod
    def get_stylesheet(dark_mode=True):
        if dark_mode:
            return f"""
            QMainWindow {{
                background-color: {ThemeManager.DARK_BG};
            }}
            QWidget {{
                background-color: {ThemeManager.DARK_BG};
                color: {ThemeManager.DARK_TEXT};
            }}
            QLineEdit, QTextEdit, QDateEdit, QComboBox {{
                background-color: #2A2A2A;
                color: {ThemeManager.DARK_TEXT};
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }}
            QLineEdit:focus, QTextEdit:focus, QDateEdit:focus, QComboBox:focus {{
                border: 2px solid {ThemeManager.LIGHT_ACCENT};
                background-color: #333333;
                box-shadow: 0 0 10px {ThemeManager.DARK_RED};
            }}
            QPushButton {{
                background-color: {ThemeManager.DARK_RED};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
                font-size: 12px;
                transition: all 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: #A01848;
            }}
            QPushButton:pressed {{
                background-color: #6B0F2C;
            }}
            QListWidget {{
                background-color: #2A2A2A;
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 5px;
            }}
            QListWidget::item {{
                padding: 8px;
                margin: 3px 0px;
                border-radius: 3px;
                border-left: 4px solid {ThemeManager.DARK_RED};
            }}
            QListWidget::item:hover {{
                background-color: #353535;
                border-left: 4px solid {ThemeManager.LIGHT_ACCENT};
            }}
            QListWidget::item:selected {{
                background-color: {ThemeManager.DARK_RED};
                border: 2px solid {ThemeManager.LIGHT_ACCENT};
            }}
            QLabel {{
                color: {ThemeManager.DARK_TEXT};
            }}
            QCheckBox {{
                color: {ThemeManager.DARK_TEXT};
            }}
            QCheckBox::indicator {{
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 3px;
                width: 18px;
                height: 18px;
                background-color: #2A2A2A;
            }}
            QCheckBox::indicator:hover {{
                background-color: #333333;
            }}
            QCheckBox::indicator:checked {{
                background-color: {ThemeManager.DARK_RED};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: #2A2A2A;
                color: {ThemeManager.DARK_TEXT};
                selection-background-color: {ThemeManager.DARK_RED};
            }}
            QScrollBar:vertical {{
                background-color: #2A2A2A;
                width: 12px;
                border: none;
            }}
            QScrollBar::handle:vertical {{
                background-color: {ThemeManager.DARK_RED};
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {ThemeManager.LIGHT_ACCENT};
            }}
            """
        else:
            return f"""
            QMainWindow {{
                background-color: {ThemeManager.LIGHT_BG};
            }}
            QWidget {{
                background-color: {ThemeManager.LIGHT_BG};
                color: {ThemeManager.LIGHT_TEXT};
            }}
            QLineEdit, QTextEdit, QDateEdit, QComboBox {{
                background-color: #F5F5F5;
                color: {ThemeManager.LIGHT_TEXT};
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }}
            QLineEdit:focus, QTextEdit:focus, QDateEdit:focus, QComboBox:focus {{
                border: 2px solid #B8104D;
                background-color: white;
                box-shadow: 0 0 10px {ThemeManager.DARK_RED};
            }}
            QPushButton {{
                background-color: {ThemeManager.DARK_RED};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
                font-size: 12px;
                transition: all 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: #A01848;
            }}
            QPushButton:pressed {{
                background-color: #6B0F2C;
            }}
            QListWidget {{
                background-color: #F9F9F9;
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 5px;
            }}
            QListWidget::item {{
                padding: 8px;
                margin: 3px 0px;
                border-radius: 3px;
                border-left: 4px solid {ThemeManager.DARK_RED};
            }}
            QListWidget::item:hover {{
                background-color: #F0F0F0;
                border-left: 4px solid {ThemeManager.LIGHT_ACCENT};
            }}
            QListWidget::item:selected {{
                background-color: {ThemeManager.DARK_RED};
                color: white;
            }}
            QLabel {{
                color: {ThemeManager.LIGHT_TEXT};
            }}
            QCheckBox {{
                color: {ThemeManager.LIGHT_TEXT};
            }}
            QCheckBox::indicator {{
                border: 2px solid {ThemeManager.DARK_RED};
                border-radius: 3px;
                width: 18px;
                height: 18px;
                background-color: white;
            }}
            QCheckBox::indicator:hover {{
                background-color: #F5F5F5;
            }}
            QCheckBox::indicator:checked {{
                background-color: {ThemeManager.DARK_RED};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: #F5F5F5;
                color: {ThemeManager.LIGHT_TEXT};
                selection-background-color: {ThemeManager.DARK_RED};
            }}
            QScrollBar:vertical {{
                background-color: #F5F5F5;
                width: 12px;
                border: none;
            }}
            QScrollBar::handle:vertical {{
                background-color: {ThemeManager.DARK_RED};
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {ThemeManager.LIGHT_ACCENT};
            }}
            """


class AnimatedListItem(QListWidgetItem):
    """Custom list item with animation support"""
    def __init__(self, text):
        super().__init__(text)
        self.animation_in_progress = False


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()
        self.dark_mode = True
        self.setWindowTitle("TODO App")
        self.setMinimumSize(600, 700)
        self.setGeometry(100, 100, 900, 800)
        
        # Optimize memory usage
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)
        
        # Header with title and theme toggle
        header_layout = QHBoxLayout()
        title_label = QLabel("TODO App")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        
        theme_btn = QPushButton("🌙 Dark")
        theme_btn.setMaximumWidth(100)
        theme_btn.clicked.connect(self.toggle_theme)
        self.theme_btn = theme_btn
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(theme_btn)
        main_layout.addLayout(header_layout)
        
        # Input section
        input_frame = QFrame()
        input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        input_layout = QVBoxLayout()
        input_layout.setSpacing(8)
        
        input_label = QLabel("Task to Add")
        task_font = QFont()
        task_font.setPointSize(11)
        task_font.setBold(True)
        input_label.setFont(task_font)
        
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter task title...")
        self.task_input.returnPressed.connect(self.add_task)
        
        desc_label = QLabel("Description for task")
        desc_label.setFont(task_font)
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Enter task description (optional)...")
        self.desc_input.setMaximumHeight(60)
        
        # Priority and Due Date section
        options_layout = QHBoxLayout()
        options_layout.setSpacing(10)
        
        priority_label = QLabel("Priority")
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Low", "Medium", "High"])
        self.priority_combo.setCurrentText("Medium")
        
        due_date_label = QLabel("Due Date")
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        
        options_layout.addWidget(priority_label)
        options_layout.addWidget(self.priority_combo)
        options_layout.addSpacing(20)
        options_layout.addWidget(due_date_label)
        options_layout.addWidget(self.date_input)
        options_layout.addStretch()
        
        # Add task button
        self.add_btn = QPushButton("+ Add Task")
        self.add_btn.setMinimumHeight(35)
        self.add_btn.clicked.connect(self.add_task)
        
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(desc_label)
        input_layout.addWidget(self.desc_input)
        input_layout.addLayout(options_layout)
        input_layout.addWidget(self.add_btn)
        
        input_frame.setLayout(input_layout)
        main_layout.addWidget(input_frame)
        
        # Sorting section
        sort_layout = QHBoxLayout()
        sort_label = QLabel("Sort by:")
        sort_font = QFont()
        sort_font.setPointSize(10)
        sort_label.setFont(sort_font)
        
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Priority", "Due Date", "Name"])
        self.sort_combo.currentTextChanged.connect(self.refresh_task_list)
        self.sort_combo.setMaximumWidth(150)
        
        sort_layout.addWidget(sort_label)
        sort_layout.addWidget(self.sort_combo)
        sort_layout.addStretch()
        main_layout.addLayout(sort_layout)
        
        # Task list
        list_label = QLabel("Lists of tasks ordered by Priority or Due Date")
        list_label.setFont(task_font)
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.toggle_task_complete)
        self.task_list.setStyleSheet("QListWidget { padding: 5px; }")
        main_layout.addWidget(list_label)
        main_layout.addWidget(self.task_list)
        
        central_widget.setLayout(main_layout)
        
        # Right-click context menu
        self.task_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.task_list.customContextMenuRequested.connect(self.show_context_menu)
        
        self.refresh_task_list()
    
    def add_task(self):
        """Add a new task with animation"""
        title = self.task_input.text().strip()
        if not title:
            QMessageBox.warning(self, "Empty Task", "Please enter a task title.")
            return
        
        description = self.desc_input.toPlainText().strip()
        priority = self.priority_combo.currentText()
        due_date = self.date_input.date().toString(Qt.DateFormat.ISODate)
        
        task = Task(title, description, priority, due_date)
        self.task_manager.add_task(task)
        
        # Clear inputs
        self.task_input.clear()
        self.desc_input.clear()
        self.priority_combo.setCurrentText("Medium")
        self.date_input.setDate(QDate.currentDate())
        
        # Visual feedback
        self.animate_button(self.add_btn)
        
        self.refresh_task_list()
    
    def animate_button(self, button):
        """Animate button press feedback"""
        original_color = button.styleSheet()
        button.setStyleSheet(original_color + "background-color: #E8B4BA;")
        QTimer.singleShot(150, lambda: button.setStyleSheet(original_color))
    
    def toggle_task_complete(self, item):
        """Toggle task completion status with animation"""
        task_id = item.data(Qt.ItemDataRole.UserRole)
        for task in self.task_manager.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                break
        self.task_manager.save_tasks()
        
        # Refresh after completion
        QTimer.singleShot(300, self.refresh_task_list)
    
    def refresh_task_list(self):
        """Refresh the task list display"""
        sort_by = self.sort_combo.currentText().lower().replace(" ", "_")
        if sort_by == "priority":
            tasks = self.task_manager.get_sorted_tasks('priority')
        elif sort_by == "due_date":
            tasks = self.task_manager.get_sorted_tasks('due_date')
        else:
            tasks = self.task_manager.get_sorted_tasks('name')
        
        self.task_list.clear()
        
        for idx, task in enumerate(tasks):
            # Create task display string
            completed_marker = "✓" if task.completed else "○"
            priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(task.priority, "")
            
            text = f"{completed_marker} {task.title} {priority_emoji}\n   Due: {task.due_date} | {task.priority}"
            if task.description:
                text += f"\n   {task.description[:50]}{'...' if len(task.description) > 50 else ''}"
            
            item = AnimatedListItem(text)
            item.setData(Qt.ItemDataRole.UserRole, task.id)
            
            # Style completed tasks
            if task.completed:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
                item.setForeground(QColor(128, 128, 128))
            
            self.task_list.addItem(item)
    
    def show_context_menu(self, position):
        """Show context menu for task deletion"""
        item = self.task_list.itemAt(position)
        if item:
            menu = QMenu()
            delete_action = menu.addAction("Delete Task")
            action = menu.exec(self.task_list.mapToGlobal(position))
            if action == delete_action:
                self.delete_task(item.data(Qt.ItemDataRole.UserRole))
    
    def delete_task(self, task_id):
        """Delete a task"""
        self.task_manager.remove_task(task_id)
        self.refresh_task_list()
    
    def toggle_theme(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()
    
    def apply_theme(self):
        """Apply theme stylesheet"""
        stylesheet = ThemeManager.get_stylesheet(self.dark_mode)
        self.setStyleSheet(stylesheet)
        
        # Update theme button text
        mode_text = "☀️ Light" if self.dark_mode else "🌙 Dark"
        self.theme_btn.setText(mode_text)
    
    def resizeEvent(self, event):
        """Handle window resize for responsive design"""
        super().resizeEvent(event)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TODO App")
    window = TodoApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
