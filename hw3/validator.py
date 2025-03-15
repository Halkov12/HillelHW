
from webargs import fields, validate

generate_students_validator = {
        'count': fields.Int(
            missing=5,
            validate=[validate.Range(min=1, max=1000)]
        ),
    }

bitcoin_value_validator = {
        'currency': fields.Str(
            missing="USD"
        ),
        'convert': fields.Int(
            missing=1,
            validate=validate.Range(min=1)
        ),
    }