from selenium.webdriver.common.by import By
import time
import calendar
from RPA.Browser.Selenium import Selenium
from selenium.common.exceptions import NoSuchElementException

br = Selenium()

def month_to_number(month):
    """
    Convert month name to its corresponding number.

    Args:
        month (str): The name of the month.

    Returns:
        int: The month number.
    """
    month_names = calendar.month_name[1:]  
   
    if month in month_names:
        month_number = month_names.index(month) + 1
    else:
        month_number = None
    
    return month_number
        


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        # Greet the user
        print("Hello, my name is " + self.name)
        
    def steps_to_take(self):
        """
        Explain steps to take for the robot.
        """
        print("\nI am a Robotic Researcher. I would be displaying key information details about famous scientists. These details include their name, birth date, death date, age at death, and the first paragraph of their Wikipedia pages. This, I would do by opening a web browser and navigating to wikipedia in the same manner a human would. Join me on this amazing journey!")

    def say_goodbye(self):
        # Bid farewell
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        """
        Open a webpage in a web browser.

        Args:
            webpage (str): The URL of the webpage to open.
        """
        br.open_available_browser(webpage)
                
    def get_scientist_info(self, scientist_name):
        """
        Retrieve information about a scientist from Wikipedia.

        Args:
            scientist_name (str): The name of the scientist.

        Returns:
            tuple: A tuple containing the scientist's birth date, death date, age, and first paragraph of their Wikipedia page.
        """
        # Search for the Scientist on Wikipedia.
        search_box = br.driver.find_element(By.ID, "searchInput")
        search_box.clear()
        search_box.send_keys(scientist_name)
        search_box.submit()
        
        # Wait for the page to load
        time.sleep(3)
        
        # Retrieve the scientist's birth date.       
        birth_date_element = br.driver.find_element(By.XPATH, '//span[@class="bday"]')
        birth_date = birth_date_element.get_attribute("innerHTML")

        # Retrieve the scientist's death date.       
        death_date_element = br.driver.find_element(By.XPATH, '//*[@class="infobox biography vcard"]//tr[th[contains(text(), "Died")]//following-sibling::td//span]')
        death_date_text = death_date_element.text.strip()
        death_date = death_date_text.replace("(", "").replace(")", "") if death_date_text else None
                        
        # Convert the death date to the format yyyy-mm-dd.
        if death_date:
            month = death_date.split(" ")[2]
            month_number = month_to_number(month)
            if month_number >= 10:
                death_date = death_date.split(" ")[3] + "-" + str(month_number) + "-" + death_date.split(" ")[1]
            death_date = death_date.split(" ")[3] + "-0" + str(month_number) + "-" + death_date.split(" ")[1]
            
        
        # Calculate the Scientist's age using the birth and death years.
        try:
            birth_year = int(birth_date.split("-")[0])
            death_year = int(death_date.split("-")[0]) if death_date and "-" in death_date else None
            age = death_year - birth_year if death_year else None
        except (AttributeError, ValueError):
            age = None
            

        # Retrive the first paragraph of the Scientist's Wikipedia page.
        first_paragraph_element = br.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')
        br.driver.implicitly_wait(10)
        first_paragraph = first_paragraph_element.text.strip() if first_paragraph_element else None
        

        """
        BONUS:
        Other nifty features could be added to the robot. Some examples of such features include:
        notable inventions, notable awards, education history, notable publications, quotes, etc.  
        """
        
        # Retrive the first award of the Scientist's biography card (bonus feature).
        award_element = br.driver.find_element(By.XPATH, '//*[@class="infobox biography vcard"]//tr[th[contains(text(), "Awards")]]//td/div/ul/li')
        notable_award = award_element.text.strip() if award_element else None
        

    
        return birth_date, death_date, age, first_paragraph, notable_award

