class TrackingService:
    @staticmethod
    def generate_tracking_pixel(email_id):
        return f'<img src="https://tracking-url.com/track?email_id={email_id}" width="1" height="1" alt="">'
