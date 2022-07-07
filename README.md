# pserial

This is a small, hand-written library for serializing and deserializing a dictionary in Python.

### Use

```python
import pserial
dictionary = {
  "id": 1,
  "first_name": "Jeanette",
  "last_name": "Penddreth",
  "email": "jpenddreth0@census.gov",
  "gender": "Female",
  "ip_address": "26.58.193.2"
}
# to serialise
pserial.serialize(dictionary)
# serialised dictionary stored in file

pserial.deserialize()
# returns the deserialized dictionary from the file
```