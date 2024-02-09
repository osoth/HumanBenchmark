import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


if __name__ == "__main__":
	options = webdriver.ChromeOptions()
	options.add_extension('/home/whoami/Documents/ChromeExtensions/uBlock Origin 1.55.0.0.crx')
	options.add_extension("/home/whoami/Documents/ChromeExtensions/I don't care about cookies 3.5.0.0.crx")
	driver = webdriver.Chrome(options=options)
	driver.get("https://humanbenchmark.com/tests/typing")
	driver.maximize_window()
	time.sleep(2)
	# Find the parent <div> element
	parent_div = driver.find_element(By.CLASS_NAME, 'letters')

	# Find all child <span> elements
	letters_spans = parent_div.find_elements(By.TAG_NAME, 'span')
	actions = ActionChains(driver)

	# Loop through each <span> element
	for span in letters_spans:
		# Extract text from span and handle exceptions
		if span.text == 'z':
			text = 'y'
		elif span.text == 'y':
			text = 'z'
		else:
			text = span.text if span.text else ' '  # Replace empty text with space

		# Perform key press action with the specified text
		actions.send_keys(text)

	# Perform all actions
	actions.perform()
	a = input()
	if len(a) > 0:
		driver.quit()

