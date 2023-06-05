# +7(812)DDD-DDDD,+7(812)DDD-DD-DD,+7(921)DDD-DDDD,+7(921)DDD-DD-DD

import re
numbers = '+7(812)123-2353, +7(812)353-33-22, +7(921)245-9583, 8(123)243-123-1, +7(921)431-12-12'
regex = r'\+7\(812\)\d{3}-\d{2}-\d{2}|\+7\(812\)\d{3}-\d{4}|\+7\(921\)\d{3}-\d{2}-\d{2}|\+7\(921\)\d{3}-\d{4}'
phone = re.findall(regex, numbers)
print(*phone, sep='\n')