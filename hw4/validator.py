from webargs import fields, validate

order_price_validator = {
        'country': fields.Str(
            missing=None
        ),
    }

track_id_validator = {
        'track_id': fields.Int(),
    }
