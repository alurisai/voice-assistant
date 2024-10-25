from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class music:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Ensure you have the path to the ChromeDriver if necessary

    def play(self, query):
        try:
            self.driver.get(f"https://www.youtube.com/results?search_query={query}")

            # Wait for the video titles to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "video-title"))
            )

            # Locate the video element
            video = self.driver.find_element(By.XPATH, '//a[@id="video-title"]')
            if video:
                video.click()
            else:
                print("No video found for the query")
                return

            time.sleep(5)  # Give it some time to load, adjust if necessary

            # Wait until the video has loaded and starts to play
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'html5-video-player'))
            )

            # Actively check if video is playing and wait until it finishes
            video_started = False
            while True:
                try:
                    current_time = self.driver.execute_script(
                        "return document.querySelector('.html5-video-player').getCurrentTime()"
                    )
                    duration = self.driver.execute_script(
                        "return document.querySelector('.html5-video-player').getDuration()"
                    )
                    if current_time > 0:
                        video_started = True
                    if video_started and current_time >= duration:
                        break
                    time.sleep(5)  # Check every 5 seconds
                except NoSuchWindowException:
                    print("Browser window closed manually.")
                    break
                except WebDriverException as e:
                    print(f"Ignoring WebDriverException while waiting for video to finish: {e}")
                    time.sleep(5)
                except Exception as e:
                    print(f"Error while waiting for video to finish: {e}")
                    break

        except (NoSuchElementException, WebDriverException) as e:
            print(f"Failed to play video: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.close()

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error closing the driver: {e}")

