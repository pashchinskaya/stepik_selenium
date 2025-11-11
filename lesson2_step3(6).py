from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


# Функция для вычисления капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Запоминаем текущую вкладку
    original_window = browser.current_window_handle
    print(f"Текущая вкладка: {original_window}")

    # Нажимаем на кнопку
    browser.find_element(By.TAG_NAME, "button").click()

    # Ждем открытия новой вкладки
    time.sleep(1)

    # Находим все открытые вкладки
    all_windows = browser.window_handles

    # Переключаемся на новую вкладку (та, которая не исходная)
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break

    print(f"Переключились на вкладку: {browser.current_window_handle}")

    # Решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)

    # Вводим ответ и отправляем
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Получаем ответ из alert
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(f"Ответ: {answer}")
    alert.accept()

finally:
    time.sleep(1)
    browser.quit()