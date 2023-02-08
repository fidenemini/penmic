import zapv2
import time

# Define the target website to scan
target = 'http://example.com'

# Define the OWASP Top 10 risks to check for
risks = [
    'A01:2021-Broken Access Control',
    'A02:2021-Cryptographic Failures',
    'A03:2021-Injection',
    'A04:2021-Insecure Direct Object References',
    'A05:2021-Security Misconfiguration',
    'A06:2021-Sensitive Data Exposure',
    'A07:2021-Missing Function Level Access Control',
    'A08:2021-Cross-Site Request Forgery (CSRF)',
    'A09:2021-Using Components with Known Vulnerabilities',
    'A10:2021-Insufficient Logging and Monitoring'
]

# Start ZAP
zap = zapv2.ZAPv2(apikey='api-key')

# Spider the target
print('Spidering target %s' % target)
zap.spider.scan(target)

# Wait for the spider to finish
while (int(zap.spider.status(target)) < 100):
    print('Spider progress %: ' + zap.spider.status(target))
    time.sleep(2)

# Run an active scan on the target
print('Active scanning target %s' % target)
zap.ascan.scan(target)

# Wait for the active scan to finish
while (int(zap.ascan.status(target)) < 100):
    print('Active scan progress %: ' + zap.ascan.status(target))
    time.sleep(5)

# Get the alerts from the scan
alerts = zap.core.alerts()

# Check for the OWASP Top 10 risks
for risk in risks:
    for alert in alerts:
        if risk in alert.get('name'):
            print('Risk found: ' + risk + ' at URL: ' + alert.get('url'))

# Stop ZAP
zap.core.shutdown()