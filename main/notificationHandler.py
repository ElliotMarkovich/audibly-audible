from plyer import notification


notification.notify(
    title = 'Noise Warning',
    message = 'Your current noise levels are unhealthy. Lower the volume to protect your ears.',
    app_icon = None,
    timeout = 10,
)
