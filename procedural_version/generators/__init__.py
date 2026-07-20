# Импортируем короткую функцию возраста из файла age.py.
from procedural_version.generators.age import age
# Импортируем короткую функцию года рождения из файла birth_year.py.
from procedural_version.generators.birth_year import birth_year
# Импортируем короткую функцию города из файла city.py.
from procedural_version.generators.city import city
# Импортируем короткую функцию комментария из файла comment.py.
from procedural_version.generators.comment import comment
# Импортируем короткую функцию email из файла email.py.
from procedural_version.generators.email import email
# Импортируем короткую функцию имени из файла first_name.py.
from procedural_version.generators.first_name import first_name
# Импортируем короткую функцию полного имени из файла full_name.py.
from procedural_version.generators.full_name import full_name
# Импортируем короткую функцию активности из файла active_example.py.
from procedural_version.generators.active_example import active_example
# Импортируем короткую функцию фамилии из файла last_name.py.
from procedural_version.generators.last_name import last_name
# Импортируем короткую функцию пароля из файла password.py.
from procedural_version.generators.password import password
# Импортируем короткую функцию телефона из файла phone.py.
from procedural_version.generators.phone import phone
# Импортируем короткую функцию даты регистрации из файла reg_date_example.py.
from procedural_version.generators.reg_date_example import reg_date_example
# Импортируем короткую функцию балла из файла score_example.py.
from procedural_version.generators.score_example import score_example
# Импортируем короткую функцию плана подписки из файла plan_example.py.
from procedural_version.generators.plan_example import plan_example
# Импортируем короткую функцию тегов из файла tags.py.
from procedural_version.generators.tags import tags
# Импортируем короткую функцию ID из файла user_id.py.
from procedural_version.generators.user_id import user_id
# Импортируем короткую функцию username из файла username.py.
from procedural_version.generators.username import username
# Импортируем короткую функцию профиля из файла user_profile.py.
from procedural_version.generators.user_profile import user_profile

# Перечисляем короткие имена, которые удобно импортировать ученикам.
__all__ = [
    # Короткое имя для генерации ID.
    "user_id",
    # Короткое имя для генерации имени.
    "first_name",
    # Короткое имя для генерации фамилии.
    "last_name",
    # Короткое имя для генерации полного имени.
    "full_name",
    # Короткое имя для генерации возраста.
    "age",
    # Короткое имя для генерации года рождения.
    "birth_year",
    # Короткое имя для генерации балла.
    "score_example",
    # Короткое имя для генерации активности.
    "active_example",
    # Короткое имя для генерации плана подписки.
    "plan_example",
    # Короткое имя для генерации даты регистрации.
    "reg_date_example",
    # Короткое имя для генерации города.
    "city",
    # Короткое имя для генерации телефона.
    "phone",
    # Короткое имя для генерации email.
    "email",
    # Короткое имя для генерации username.
    "username",
    # Короткое имя для генерации комментария.
    "comment",
    # Короткое имя для генерации пароля.
    "password",
    # Короткое имя для генерации тегов.
    "tags",
    # Короткое имя для генерации профиля.
    "user_profile",
]
