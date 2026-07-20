# Импортируем модуль unittest, чтобы писать автоматические тесты.
import unittest
# Импортируем список имен для простой проверки.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для простой проверки.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов для простой проверки.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список тегов для простой проверки.
from procedural_version.data.names_data import TAGS
# Импортируем список планов подписки для простой проверки.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем функцию генерации возраста.
from procedural_version.generators.age import age as age_fn
# Импортируем функцию генерации года рождения.
from procedural_version.generators.birth_year import birth_year as birth_year_fn
# Импортируем функцию генерации города.
from procedural_version.generators.city import city as city_fn
# Импортируем функцию генерации комментария.
from procedural_version.generators.comment import comment as comment_fn
# Импортируем функцию генерации email.
from procedural_version.generators.email import email as email_fn
# Импортируем функцию генерации имени.
from procedural_version.generators.first_name import first_name as first_name_fn
# Импортируем функцию генерации полного имени.
from procedural_version.generators.full_name import full_name as full_name_fn
# Импортируем пример готовой функции генерации активности.
from procedural_version.generators.active_example import active_example as active_fn
# Импортируем функцию генерации фамилии.
from procedural_version.generators.last_name import last_name as last_name_fn
# Импортируем функцию генерации пароля.
from procedural_version.generators.password import password as password_fn
# Импортируем функцию генерации телефона.
from procedural_version.generators.phone import phone as phone_fn
# Импортируем пример готовой функции генерации даты регистрации.
from procedural_version.generators.reg_date_example import reg_date_example as reg_date_fn
# Импортируем пример готовой функции генерации балла.
from procedural_version.generators.score_example import score_example as score_fn
# Импортируем пример готовой функции генерации плана подписки.
from procedural_version.generators.plan_example import plan_example as plan_fn
# Импортируем функцию генерации тегов.
from procedural_version.generators.tags import tags as tags_fn
# Импортируем функцию генерации ID.
from procedural_version.generators.user_id import user_id as user_id_fn
# Импортируем функцию генерации профиля.
from procedural_version.generators.user_profile import user_profile as user_profile_fn
# Импортируем функцию генерации username.
from procedural_version.generators.username import username as username_fn

# Объявляем класс с тестами процедурной версии.
class ProceduralGeneratorsTest(unittest.TestCase):
    # Объявляем тест ID заданной длины.
    def test_id_digits(self):
        # Генерируем ID длиной 8 символов.
        user_id = user_id_fn(length=8, seed=1)
        # Проверяем, что ID является строкой.
        self.assertIsInstance(user_id, str)
        # Проверяем, что ID имеет ровно 8 символов.
        self.assertEqual(len(user_id), 8)
        # Проверяем, что ID состоит только из цифр.
        self.assertTrue(user_id.isdigit())

    # Объявляем тест ID с буквами и цифрами.
    def test_id_alnum(self):
        # Генерируем буквенно-цифровой ID.
        user_id = user_id_fn(length=10, only_digits=False, seed=1)
        # Проверяем, что ID имеет ровно 10 символов.
        self.assertEqual(len(user_id), 10)
        # Проверяем, что ID состоит из букв и цифр.
        self.assertTrue(user_id.isalnum())

    # Объявляем тест ошибки при неправильной длине ID.
    def test_id_bad_length(self):
        # Проверяем, что длина 0 должна вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем ID с неправильной длиной.
            user_id_fn(length=0, seed=1)

    # Объявляем тест повторяемости ID при одинаковом seed.
    def test_id_seed(self):
        # Генерируем первый ID с seed=1.
        first_user_id = user_id_fn(length=8, seed=1)
        # Генерируем второй ID с таким же seed=1.
        second_user_id = user_id_fn(length=8, seed=1)
        # Проверяем, что оба ID одинаковые.
        self.assertEqual(first_user_id, second_user_id)

    # Объявляем тест имени с ограничением длины.
    def test_first_name_min_len(self):
        # Генерируем имя не короче 5 символов.
        first_name = first_name_fn(min_length=5, seed=1)
        # Проверяем, что имя взято из учебного списка.
        self.assertIn(first_name, FIRST_NAMES)
        # Проверяем, что имя не короче 5 символов.
        self.assertGreaterEqual(len(first_name), 5)

    # Объявляем тест имени с максимальной длиной.
    def test_first_name_max_len(self):
        # Генерируем имя не длиннее 4 символов.
        first_name = first_name_fn(max_length=4, seed=1)
        # Проверяем, что имя взято из учебного списка.
        self.assertIn(first_name, FIRST_NAMES)
        # Проверяем, что имя не длиннее 4 символов.
        self.assertLessEqual(len(first_name), 4)

    # Объявляем тест ошибки, если подходящих имен нет.
    def test_first_name_no_match(self):
        # Проверяем, что невозможное ограничение длины должно вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем имя длиной минимум 1000 символов.
            first_name_fn(min_length=1000, seed=1)

    # Объявляем тест повторяемости имени при одинаковом seed.
    def test_first_name_seed(self):
        # Генерируем первое имя с seed=1.
        first_name = first_name_fn(seed=1)
        # Генерируем второе имя с таким же seed=1.
        second_name = first_name_fn(seed=1)
        # Проверяем, что оба имени одинаковые.
        self.assertEqual(first_name, second_name)

    # Объявляем тест фамилии с ограничением длины.
    def test_last_name_max_len(self):
        # Генерируем фамилию не длиннее 7 символов.
        last_name = last_name_fn(max_length=7, seed=1)
        # Проверяем, что фамилия взята из учебного списка.
        self.assertIn(last_name, LAST_NAMES)
        # Проверяем, что фамилия не длиннее 7 символов.
        self.assertLessEqual(len(last_name), 7)

    # Объявляем тест фамилии с минимальной длиной.
    def test_last_name_min_len(self):
        # Генерируем фамилию не короче 8 символов.
        last_name = last_name_fn(min_length=8, seed=1)
        # Проверяем, что фамилия взята из учебного списка.
        self.assertIn(last_name, LAST_NAMES)
        # Проверяем, что фамилия не короче 8 символов.
        self.assertGreaterEqual(len(last_name), 8)

    # Объявляем тест ошибки, если подходящих фамилий нет.
    def test_last_name_no_match(self):
        # Проверяем, что невозможное ограничение длины должно вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем фамилию длиной минимум 1000 символов.
            last_name_fn(min_length=1000, seed=1)

    # Объявляем тест повторяемости фамилии при одинаковом seed.
    def test_last_name_seed(self):
        # Генерируем первую фамилию с seed=1.
        first_last_name = last_name_fn(seed=1)
        # Генерируем вторую фамилию с таким же seed=1.
        second_last_name = last_name_fn(seed=1)
        # Проверяем, что обе фамилии одинаковые.
        self.assertEqual(first_last_name, second_last_name)

    # Объявляем тест полного имени с максимальной длиной.
    def test_full_name_max_len(self):
        # Генерируем полное имя с ограничением общей длины.
        full_name = full_name_fn(max_total_length=10, seed=1)
        # Проверяем, что полное имя не длиннее 10 символов.
        self.assertLessEqual(len(full_name), 10)

    # Объявляем тест полного имени без ограничения длины.
    def test_full_name_basic(self):
        # Генерируем полное имя без ограничения длины.
        full_name = full_name_fn(seed=1)
        # Проверяем, что результат является строкой.
        self.assertIsInstance(full_name, str)
        # Проверяем, что внутри есть пробел между именем и фамилией.
        self.assertIn(" ", full_name)

    # Объявляем тест повторяемости полного имени при одинаковом seed.
    def test_full_name_seed(self):
        # Генерируем первое полное имя с seed=1.
        first_full_name = full_name_fn(seed=1)
        # Генерируем второе полное имя с таким же seed=1.
        second_full_name = full_name_fn(seed=1)
        # Проверяем, что оба полных имени одинаковые.
        self.assertEqual(first_full_name, second_full_name)

    # Объявляем тест возраста на границах.
    def test_age_bounds(self):
        # Проверяем нижнюю границу возраста.
        self.assertEqual(age_fn(min_age=18, max_age=80, boundary="min"), 18)
        # Проверяем верхнюю границу возраста.
        self.assertEqual(age_fn(min_age=18, max_age=80, boundary="max"), 80)
        # Проверяем значение ниже нижней границы.
        self.assertEqual(age_fn(min_age=18, max_age=80, boundary="below_min"), 17)
        # Проверяем значение выше верхней границы.
        self.assertEqual(age_fn(min_age=18, max_age=80, boundary="above_max"), 81)

    # Объявляем тест обычного возраста внутри диапазона.
    def test_age_range(self):
        # Генерируем обычный возраст без boundary.
        age = age_fn(min_age=18, max_age=80, seed=1)
        # Проверяем, что возраст не меньше нижней границы.
        self.assertGreaterEqual(age, 18)
        # Проверяем, что возраст не больше верхней границы.
        self.assertLessEqual(age, 80)

    # Объявляем тест ошибки при неправильном диапазоне возраста.
    def test_age_bad_range(self):
        # Проверяем, что перепутанные границы должны вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем возраст с неправильным диапазоном.
            age_fn(min_age=80, max_age=18, seed=1)

    # Объявляем тест повторяемости возраста при одинаковом seed.
    def test_age_seed(self):
        # Генерируем первый возраст с seed=1.
        first_age = age_fn(seed=1)
        # Генерируем второй возраст с таким же seed=1.
        second_age = age_fn(seed=1)
        # Проверяем, что оба возраста одинаковые.
        self.assertEqual(first_age, second_age)

    # Объявляем тест года рождения на границах.
    def test_birth_year_bounds(self):
        # Проверяем нижнюю границу года рождения.
        self.assertEqual(birth_year_fn(min_year=1950, max_year=2008, boundary="min"), 1950)
        # Проверяем верхнюю границу года рождения.
        self.assertEqual(birth_year_fn(min_year=1950, max_year=2008, boundary="max"), 2008)
        # Проверяем значение ниже нижней границы.
        self.assertEqual(birth_year_fn(min_year=1950, max_year=2008, boundary="below_min"), 1949)
        # Проверяем значение выше верхней границы.
        self.assertEqual(birth_year_fn(min_year=1950, max_year=2008, boundary="above_max"), 2009)

    # Объявляем тест обычного года рождения внутри диапазона.
    def test_birth_year_range(self):
        # Генерируем обычный год рождения без boundary.
        birth_year = birth_year_fn(min_year=1950, max_year=2008, seed=1)
        # Проверяем, что год не меньше нижней границы.
        self.assertGreaterEqual(birth_year, 1950)
        # Проверяем, что год не больше верхней границы.
        self.assertLessEqual(birth_year, 2008)

    # Объявляем тест ошибки при неправильном диапазоне года рождения.
    def test_birth_year_bad_range(self):
        # Проверяем, что перепутанные годы должны вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем год рождения с неправильным диапазоном.
            birth_year_fn(min_year=2008, max_year=1950, seed=1)

    # Объявляем тест повторяемости года рождения при одинаковом seed.
    def test_birth_year_seed(self):
        # Генерируем первый год рождения с seed=1.
        first_birth_year = birth_year_fn(seed=1)
        # Генерируем второй год рождения с таким же seed=1.
        second_birth_year = birth_year_fn(seed=1)
        # Проверяем, что оба года одинаковые.
        self.assertEqual(first_birth_year, second_birth_year)

    # Объявляем тест города с фильтром по началу строки.
    def test_city_prefix(self):
        # Генерируем город, который начинается с буквы М.
        city = city_fn(starts_with="М", seed=1)
        # Проверяем, что город взят из учебного списка.
        self.assertIn(city, CITY_NAMES)
        # Проверяем, что город начинается с нужной буквы.
        self.assertTrue(city.startswith("М"))

    # Объявляем тест ошибки, если городов с таким началом нет.
    def test_city_bad_prefix(self):
        # Проверяем, что неизвестное начало города должно вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем город с началом, которого нет в списке.
            city_fn(starts_with="@@@", seed=1)

    # Объявляем тест обычного города из списка.
    def test_city_list(self):
        # Генерируем город без фильтра.
        city = city_fn(seed=1)
        # Проверяем, что город взят из учебного списка.
        self.assertIn(city, CITY_NAMES)

    # Объявляем тест повторяемости города при одинаковом seed.
    def test_city_seed(self):
        # Генерируем первый город с seed=1.
        first_city = city_fn(seed=1)
        # Генерируем второй город с таким же seed=1.
        second_city = city_fn(seed=1)
        # Проверяем, что оба города одинаковые.
        self.assertEqual(first_city, second_city)

    # Объявляем тест комментария точной длины.
    def test_comment_len(self):
        # Генерируем комментарий длиной 255 символов.
        comment = comment_fn(length=255, seed=1)
        # Проверяем, что комментарий является строкой.
        self.assertIsInstance(comment, str)
        # Проверяем, что длина комментария ровно 255 символов.
        self.assertEqual(len(comment), 255)

    # Объявляем тест комментариев разной длины.
    def test_comment_lengths(self):
        # Проверяем комментарий нулевой длины.
        self.assertEqual(len(comment_fn(length=0, seed=1)), 0)
        # Проверяем комментарий длиной 1 символ.
        self.assertEqual(len(comment_fn(length=1, seed=1)), 1)
        # Проверяем комментарий большой длины.
        self.assertEqual(len(comment_fn(length=1000, seed=1)), 1000)

    # Объявляем тест ошибки при отрицательной длине комментария.
    def test_comment_bad_len(self):
        # Проверяем, что отрицательная длина должна вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем комментарий с отрицательной длиной.
            comment_fn(length=-1, seed=1)

    # Объявляем тест повторяемости комментария при одинаковом seed.
    def test_comment_seed(self):
        # Генерируем первый комментарий с seed=1.
        first_comment = comment_fn(length=100, seed=1)
        # Генерируем второй комментарий с таким же seed=1.
        second_comment = comment_fn(length=100, seed=1)
        # Проверяем, что оба комментария одинаковые.
        self.assertEqual(first_comment, second_comment)

    # Объявляем тест email в валидном и невалидном режиме.
    def test_email_validity(self):
        # Генерируем валидный email.
        valid_email = email_fn(valid=True, username_length=8, seed=1)
        # Генерируем невалидный email.
        invalid_email = email_fn(valid=False, username_length=8, seed=1)
        # Проверяем, что в валидном email есть знак собаки.
        self.assertIn("@", valid_email)
        # Проверяем, что в невалидном email нет знака собаки.
        self.assertNotIn("@", invalid_email)
        # Проверяем, что часть до знака собаки имеет нужную длину.
        self.assertEqual(len(valid_email.split("@")[0]), 8)

    # Объявляем тест ошибки при неправильной длине username в email.
    def test_email_bad_len(self):
        # Проверяем, что длина 0 должна вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем email с неправильной длиной username.
            email_fn(username_length=0, seed=1)

    # Объявляем тест повторяемости email при одинаковом seed.
    def test_email_seed(self):
        # Генерируем первый email с seed=1.
        first_email = email_fn(seed=1)
        # Генерируем второй email с таким же seed=1.
        second_email = email_fn(seed=1)
        # Проверяем, что оба email одинаковые.
        self.assertEqual(first_email, second_email)

    # Объявляем тест username точной длины.
    def test_username_len(self):
        # Генерируем username длиной 12 символов.
        username = username_fn(length=12, seed=1)
        # Проверяем, что username имеет ровно 12 символов.
        self.assertEqual(len(username), 12)

    # Объявляем тест ошибки при неправильной длине username.
    def test_username_bad_len(self):
        # Проверяем, что длина 0 должна вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем username с неправильной длиной.
            username_fn(length=0, seed=1)

    # Объявляем тест повторяемости username при одинаковом seed.
    def test_username_seed(self):
        # Генерируем первый username с seed=1.
        first_username = username_fn(length=12, seed=1)
        # Генерируем второй username с таким же seed=1.
        second_username = username_fn(length=12, seed=1)
        # Проверяем, что оба username одинаковые.
        self.assertEqual(first_username, second_username)

    # Объявляем тест пароля с цифрами и спецсимволами.
    def test_password_parts(self):
        # Генерируем пароль длиной 16 символов.
        password = password_fn(length=16, use_digits=True, use_symbols=True, seed=1)
        # Проверяем, что пароль имеет ровно 16 символов.
        self.assertEqual(len(password), 16)
        # Проверяем, что в пароле есть хотя бы одна цифра.
        self.assertTrue(any(symbol.isdigit() for symbol in password))
        # Проверяем, что в пароле есть хотя бы один спецсимвол.
        self.assertTrue(any(symbol in "!@#$%^&*" for symbol in password))

    # Объявляем тест ошибки при неправильной длине пароля.
    def test_password_bad_len(self):
        # Проверяем, что длина 0 должна вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем пароль с неправильной длиной.
            password_fn(length=0, seed=1)

    # Объявляем тест повторяемости пароля при одинаковом seed.
    def test_password_seed(self):
        # Генерируем первый пароль с seed=1.
        first_password = password_fn(length=16, seed=1)
        # Генерируем второй пароль с таким же seed=1.
        second_password = password_fn(length=16, seed=1)
        # Проверяем, что оба пароля одинаковые.
        self.assertEqual(first_password, second_password)

    # Объявляем тест телефона в валидном и невалидном режиме.
    def test_phone_validity(self):
        # Генерируем валидный телефон.
        valid_phone = phone_fn(valid=True, seed=1)
        # Генерируем невалидный телефон.
        invalid_phone = phone_fn(valid=False, seed=1)
        # Проверяем правильный код страны валидного телефона.
        self.assertEqual(valid_phone["country_code"], "+7")
        # Проверяем неправильный код страны невалидного телефона.
        self.assertNotEqual(invalid_phone["country_code"], "+7")
        # Проверяем длину основной части валидного телефона.
        self.assertGreaterEqual(valid_phone["number"], 1000000)
        # Проверяем короткую основную часть невалидного телефона.
        self.assertLess(invalid_phone["number"], 1000000)

    # Объявляем тест кода оператора телефона.
    def test_phone_code(self):
        # Генерируем валидный телефон.
        valid_phone = phone_fn(valid=True, seed=1)
        # Проверяем, что код оператора не меньше 900.
        self.assertGreaterEqual(valid_phone["operator_code"], 900)
        # Проверяем, что код оператора не больше 999.
        self.assertLessEqual(valid_phone["operator_code"], 999)

    # Объявляем тест повторяемости телефона при одинаковом seed.
    def test_phone_seed(self):
        # Генерируем первый телефон с seed=1.
        first_phone = phone_fn(seed=1)
        # Генерируем второй телефон с таким же seed=1.
        second_phone = phone_fn(seed=1)
        # Проверяем, что оба телефона одинаковые.
        self.assertEqual(first_phone, second_phone)

    # Объявляем тест даты регистрации на границах.
    def test_reg_date_bounds(self):
        # Проверяем нижнюю границу даты.
        self.assertEqual(reg_date_fn(start_year=2020, end_year=2026, boundary="min"), "2020-01-01")
        # Проверяем верхнюю границу даты.
        self.assertEqual(reg_date_fn(start_year=2020, end_year=2026, boundary="max"), "2026-12-28")
        # Проверяем дату ниже нижней границы.
        self.assertEqual(reg_date_fn(start_year=2020, end_year=2026, boundary="below_min"), "2019-12-31")
        # Проверяем дату выше верхней границы.
        self.assertEqual(reg_date_fn(start_year=2020, end_year=2026, boundary="above_max"), "2027-01-01")

    # Объявляем тест обычной даты регистрации внутри диапазона.
    def test_reg_date_range(self):
        # Генерируем обычную дату без boundary.
        registration_date = reg_date_fn(start_year=2020, end_year=2026, seed=1)
        # Разделяем дату на год, месяц и день.
        year_text, month_text, day_text = registration_date.split("-")
        # Проверяем, что год не меньше нижней границы.
        self.assertGreaterEqual(int(year_text), 2020)
        # Проверяем, что год не больше верхней границы.
        self.assertLessEqual(int(year_text), 2026)
        # Проверяем, что месяц не меньше 1.
        self.assertGreaterEqual(int(month_text), 1)
        # Проверяем, что месяц не больше 12.
        self.assertLessEqual(int(month_text), 12)
        # Проверяем, что день не меньше 1.
        self.assertGreaterEqual(int(day_text), 1)
        # Проверяем, что день не больше 28.
        self.assertLessEqual(int(day_text), 28)

    # Объявляем тест повторяемости даты регистрации при одинаковом seed.
    def test_reg_date_seed(self):
        # Генерируем первую дату с seed=1.
        first_date = reg_date_fn(seed=1)
        # Генерируем вторую дату с таким же seed=1.
        second_date = reg_date_fn(seed=1)
        # Проверяем, что обе даты одинаковые.
        self.assertEqual(first_date, second_date)

    # Объявляем тест ошибки при неправильном диапазоне дат.
    def test_reg_date_bad_range(self):
        # Проверяем, что перепутанные годы должны вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем дату с неправильным диапазоном лет.
            reg_date_fn(start_year=2026, end_year=2020, seed=1)

    # Объявляем тест учебного балла на границах.
    def test_score_bounds(self):
        # Проверяем нижнюю границу балла.
        self.assertEqual(score_fn(min_score=1, max_score=100, boundary="min"), 1)
        # Проверяем верхнюю границу балла.
        self.assertEqual(score_fn(min_score=1, max_score=100, boundary="max"), 100)
        # Проверяем значение ниже нижней границы балла.
        self.assertEqual(score_fn(min_score=1, max_score=100, boundary="below_min"), 0)
        # Проверяем значение выше верхней границы балла.
        self.assertEqual(score_fn(min_score=1, max_score=100, boundary="above_max"), 101)

    # Объявляем тест обычного балла внутри диапазона.
    def test_score_range(self):
        # Генерируем обычный балл без boundary.
        score = score_fn(min_score=1, max_score=100, seed=1)
        # Проверяем, что балл не меньше нижней границы.
        self.assertGreaterEqual(score, 1)
        # Проверяем, что балл не больше верхней границы.
        self.assertLessEqual(score, 100)

    # Объявляем тест повторяемости балла при одинаковом seed.
    def test_score_seed(self):
        # Генерируем первый балл с seed=1.
        first_score = score_fn(seed=1)
        # Генерируем второй балл с таким же seed=1.
        second_score = score_fn(seed=1)
        # Проверяем, что оба балла одинаковые.
        self.assertEqual(first_score, second_score)

    # Объявляем тест ошибки при неправильном диапазоне баллов.
    def test_score_bad_range(self):
        # Проверяем, что перепутанные границы должны вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем балл с неправильным диапазоном.
            score_fn(min_score=100, max_score=1, seed=1)

    # Объявляем тест признака активности.
    def test_active_bool(self):
        # Генерируем признак активности.
        is_active = active_fn(seed=1)
        # Проверяем, что результат является булевым значением.
        self.assertIsInstance(is_active, bool)

    # Объявляем тест повторяемости активности при одинаковом seed.
    def test_active_seed(self):
        # Генерируем первое значение активности с seed=1.
        first_value = active_fn(seed=1)
        # Генерируем второе значение активности с таким же seed=1.
        second_value = active_fn(seed=1)
        # Проверяем, что оба значения одинаковые.
        self.assertEqual(first_value, second_value)

    # Объявляем тест тегов с точным количеством и уникальностью.
    def test_tags_unique(self):
        # Генерируем 5 уникальных тегов.
        tags = tags_fn(count=5, unique=True, seed=1)
        # Проверяем, что тегов ровно 5.
        self.assertEqual(len(tags), 5)
        # Проверяем, что все теги уникальны.
        self.assertEqual(len(tags), len(set(tags)))
        # Проверяем каждый тег из списка.
        for tag in tags:
            # Проверяем, что тег взят из учебного списка.
            self.assertIn(tag, TAGS)

    # Объявляем тест ошибки при отрицательном количестве тегов.
    def test_tags_bad_count(self):
        # Проверяем, что отрицательное количество должно вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем теги с отрицательным количеством.
            tags_fn(count=-1, seed=1)

    # Объявляем тест тегов с разрешенными повторами.
    def test_tags_dupes(self):
        # Генерируем теги с разрешенными повторами.
        tags = tags_fn(count=10, unique=False, seed=1)
        # Проверяем, что тегов ровно 10.
        self.assertEqual(len(tags), 10)
        # Проверяем каждый тег из списка.
        for tag in tags:
            # Проверяем, что тег взят из учебного списка.
            self.assertIn(tag, TAGS)

    # Объявляем тест повторяемости тегов при одинаковом seed.
    def test_tags_seed(self):
        # Генерируем первый список тегов с seed=1.
        first_tags = tags_fn(count=5, unique=True, seed=1)
        # Генерируем второй список тегов с таким же seed=1.
        second_tags = tags_fn(count=5, unique=True, seed=1)
        # Проверяем, что оба списка одинаковые.
        self.assertEqual(first_tags, second_tags)

    # Объявляем тест плана подписки из разрешенного списка.
    def test_plan_allowed(self):
        # Генерируем план подписки только из двух разрешенных вариантов.
        plan = plan_fn(allowed_plans=["free", "premium"], seed=1)
        # Проверяем, что план подписки входит в разрешенный список.
        self.assertIn(plan, ["free", "premium"])

    # Объявляем тест плана подписки из общего списка.
    def test_plan_default(self):
        # Генерируем план подписки из общего списка.
        plan = plan_fn(seed=1)
        # Проверяем, что план подписки входит в общий список.
        self.assertIn(plan, SUBSCRIPTION_PLANS)

    # Объявляем тест повторяемости плана подписки при одинаковом seed.
    def test_plan_seed(self):
        # Генерируем первый план подписки с seed=1.
        first_plan = plan_fn(seed=1)
        # Генерируем второй план подписки с таким же seed=1.
        second_plan = plan_fn(seed=1)
        # Проверяем, что оба плана одинаковые.
        self.assertEqual(first_plan, second_plan)

    # Объявляем тест ошибки при пустом списке планов подписки.
    def test_plan_empty(self):
        # Проверяем, что пустой список должен вызывать ошибку.
        with self.assertRaises(ValueError):
            # Генерируем план подписки из пустого списка.
            plan_fn(allowed_plans=[], seed=1)

    # Объявляем тест профиля пользователя.
    def test_user_profile_fields(self):
        # Генерируем валидный профиль.
        profile = user_profile_fn(valid=True, seed=1)
        # Проверяем, что профиль является словарем.
        self.assertIsInstance(profile, dict)
        # Проверяем, что ID имеет длину 6 символов.
        self.assertEqual(len(profile["user_id"]), 6)
        # Проверяем, что email валидного профиля содержит знак собаки.
        self.assertIn("@", profile["email"])
        # Проверяем, что пароль имеет длину 12 символов.
        self.assertEqual(len(profile["password"]), 12)
        # Проверяем, что в профиле ровно 3 тега.
        self.assertEqual(len(profile["tags"]), 3)
        # Создаем список обязательных ключей профиля.
        required_keys = [
            "user_id",
            "first_name",
            "last_name",
            "age",
            "city",
            "is_active",
            "username",
            "email",
            "password",
            "tags",
            "registration_date",
            "subscription_plan",
        ]
        # Проверяем каждый обязательный ключ.
        for key in required_keys:
            # Проверяем, что ключ есть в профиле.
            self.assertIn(key, profile)
        # Проверяем, что username имеет длину 10 символов.
        self.assertEqual(len(profile["username"]), 10)
        # Проверяем, что признак активности имеет тип bool.
        self.assertIsInstance(profile["is_active"], bool)

    # Объявляем тест невалидного профиля пользователя.
    def test_user_profile_invalid_email(self):
        # Генерируем профиль с невалидным email.
        profile = user_profile_fn(valid=False, seed=1)
        # Проверяем, что email намеренно не содержит знак собаки.
        self.assertNotIn("@", profile["email"])

    # Объявляем тест повторяемости профиля при одинаковом seed.
    def test_user_profile_seed(self):
        # Генерируем первый профиль с seed=1.
        first_profile = user_profile_fn(valid=False, seed=1)
        # Генерируем второй профиль с таким же seed=1.
        second_profile = user_profile_fn(valid=False, seed=1)
        # Проверяем, что оба профиля одинаковые.
        self.assertEqual(first_profile, second_profile)

# Проверяем, что файл тестов запущен напрямую.
if __name__ == "__main__":
    # Запускаем тесты из этого файла.
    unittest.main()
