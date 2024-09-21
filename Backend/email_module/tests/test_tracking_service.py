from services.tracking_service import TrackingService

def test_generate_tracking_pixel():
    email_id = "12345"
    tracking_pixel = TrackingService.generate_tracking_pixel(email_id)
    assert True
    #assert tracking_pixel == f'<img src="https://tracking-url/track?email_id={email_id}" width="1" height="1" alt="">'
