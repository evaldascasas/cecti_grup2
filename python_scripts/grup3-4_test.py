try:
    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from faker import Faker
    import time
except ImportError as e:
    print(f"ImportError {e}")

class AacWebsiteTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
            self.fake = Faker('es_ES')
        except NameError as e:
            print(f"NameError {e}")

    def test_contact_form_invalid_email_field_evaldas(self):
        try:
            driver = self.driver
            contact_form_url = "http://www.aac.com/contacte/"
            driver.get(contact_form_url)

            # Introduir nom al camp del nom.
            elem = driver.find_element(By.ID, "wpforms-30-field_1")
            elem.send_keys(self.fake.name())

            # Introduir email erroni al camp del email.
            elem = driver.find_element(By.ID, "wpforms-30-field_2")
            elem.send_keys(self.fake.name())

            # Enviar la tecla ENTER per a que realitzi la validació del camp del email.
            elem.send_keys(Keys.RETURN)

            # Comparar el text de l'element on es mostra el missatge d'error.
            elem = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "wpforms-30-field_2-error"))
            )
            result = elem.text
            self.assertEqual(result, "Por favor, introduce una dirección de correo electrónico válida.")

            # Comprovar si encara seguim a la pàgina del formulari de contacte.
            self.assertEqual(driver.current_url, contact_form_url)
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def test_meta_tag_description_erick(self):
        try:
            # url = "http://192.168.20.11"
            url = "http://www.aac.com"

            driver = self.driver

            # Carregar la pàgina
            driver.get(url)

            # Buscar l'etiqueta <meta> amb l'atribut name="description"
            meta_description = driver.find_elements("xpath", "//meta[@name='description']")

            if meta_description:
                print("La pàgina conté un meta tag description.")
                print("Contingut:", meta_description[0].get_attribute("content"))
            else:
                print("La pàgina NO conté un meta tag description.")

            # Tancar el navegador
            # driver.quit()
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def test_comprova_contador_betlem(self):
        try:
            # Configuració del controlador de Chrome
            # options = Options()

            driver = self.driver

            url = "http://www.aac.com/els-nostres-preus/"

            # Crear el navegador
            # driver = webdriver.Chrome(options=options)

            # try:
            # Accedir a la pàgina passada com a paràmetre
            driver.get(url)

            # Seleccionem body per a baixar a veure el comptador
            quadrat = driver.find_element(By.XPATH, '//body')
            quadrat.send_keys(Keys.END)

            # Seleccionem la classe on estan els números
            elements = driver.find_elements(By.CLASS_NAME, 'elementor-counter-number')

            # Esperem 5 segons per a que es carregui bé la pàgina i els números arribin al màxim
            time.sleep(5)

            # Comparació: agafem l'últim element (el 18) que és el de 1,500
            if elements[-1].text == "1,500":
                print('Correcte')
            else:
                print("Incorrecte")
        # finally:
            # Tancar el navegador
            # driver.quit()
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def test_comprovacio_error_camp_nom_nasim(self):
        try:
            driver = self.driver
            # Accedir a la pàgina del login
            driver.get("http://www.aac.com/contacte/")
                
            # Localitzar i fer clic al botón de login utilitzant l'ID
            login_button = driver.find_element(By.ID, "wpforms-submit-30")  # Usamos el ID del botón
            driver.execute_script("arguments[0].scrollIntoView();", login_button)
            time.sleep(1)
            login_button.click()
            time.sleep(1)
            # Esperar a que la página cargui desprès del login

            # Verificar que el login ha donat error
            em_error_element = driver.find_element(By.ID, "wpforms-30-field_1-error")
            error_text = em_error_element.text
            assert error_text == "Este campo es obligatorio.", f"Error: el text trobat és '{error_text}'"
            print("L'inici de sessió va ser un èxit.")

        # finally:
            # Tancar el navegador
            # driver.quit()
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def test_form_contact_pol(self):
        try:
            driver = self.driver
            
            # driver.get("http://www.aac.com")
            # time.sleep(0.5)

            # contact_link = driver.find_element(By.XPATH, '//a[text()="Contacte"]')
            # contact_link.click()
            # time.sleep(2)

            driver.get("http://www.aac.com/contacte")

            name_field = driver.find_element(By.ID, "wpforms-30-field_1")
            name_field.send_keys("Pol Obalat")

            email_field = driver.find_element(By.ID, "wpforms-30-field_2")
            email_field.send_keys("polobalat@iesmontsia.org")

            message_field = driver.find_element(By.ID, "wpforms-30-field_3")
            message_field.send_keys("Provaaa")

            submit_button = driver.find_element(By.ID, "wpforms-submit-30")
            driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            time.sleep(1)
            submit_button.click()

            time.sleep(5)
            
            result_element = driver.find_element(By.XPATH, '//p[text()="¡Gracias por contactar con nosotros! Nos pondremos en contacto contigo muy pronto."]')
            result_text = result_element.text
            
            assert result_text == "¡Gracias por contactar con nosotros! Nos pondremos en contacto contigo muy pronto.", f"Error: el texto encontrado es '{result_text}'"
            # driver.quit()
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def test_percentage_jose(self):
        try:
            driver = self.driver

            driver.get("http://www.aac.com/els-nostres-preus/")
            time.sleep(2)

            divcontainer_enterprise = driver.find_element(By.CSS_SELECTOR, ".elementor-element-a43b42a")

            div_percentage = divcontainer_enterprise.find_element(By.CSS_SELECTOR, ".elementor-progress-percentage")

            print(div_percentage.text)
        except AttributeError as e:
            print(f"AttributeError {e}")
        except Exception as e:
            print(f"Exception {e}")

    def tearDown(self):
        try:
            self.driver.close()
        except AttributeError as e:
            print(f"AttributeError on tearDown {e}")

if __name__ == "__main__":
    unittest.main()
