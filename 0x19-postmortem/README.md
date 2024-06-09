# 0x19. Postmortem: Tech blog hack by Daesh

![Defaced Blog](smartmockups_lx8429fj.jpg)
<small>_Defaced blog during on-call engineer's confirmation_</small>


## Issue Summary

- Duration of the Outage:
	- Start Time: April 1, 2017, 12:00 UTC
	- End Time: April 1, 2017, 17:00 UTC
- Impact:
	- Website defaced with Daesh propaganda. 80% of users affected, experiencing a 301 redirection to the homepage. About 3 000 USD lost in ads revenue.

## Root Cause:

- A vulnerability in an outdated WordPress plugin allowed hackers to gain access and deface the site.

## Timeline

- 12:00 UTC: Monitoring alert detects unusual rate of 301 status code.
- 12:10 UTC: On-call engineer confirms the website defacement.
- 12:20 UTC: Incident escalated to the security team.
- 12:45 UTC: Security team begins identifying the vulnerability.
- 13:00 UTC: Website taken offline for containment.
- 14:00 UTC: Vulnerability traced to an outdated plugin.
- 15:00 UTC: Plugin patched and security measures updated.
- 16:00 UTC: Website restored, monitoring indicates recovery.
- 17:00 UTC: Full service confirmed restored.

## Root Cause and Resolution

### Root Cause:

- An outdated plugin contained a security flaw that was exploited by Daesh hackers to deface the website.

### Resolution:

- Patched the outdated plugin, enhanced firewall rules, and conducted a full security audit.

## Corrective and Preventative Measures

### Improvements/Fixes:

#### Security Updates:

- Implement automatic updates for plugins and software.
- Force users to login and change password

#### Monitoring and Alerts:

- Enhance real-time monitoring for suspicious activity.

#### Documentation and Training:

- Update security protocols and provide staff training on cybersecurity best practices.

## Tasks to Address the Issue:

1. Patch Vulnerable Plugin:
	- Review and update all plugins to the latest versions.
1. Enhance Security Monitoring:
	- Deploy advanced threat detection tools.
1. Develop Incident Response Plan:
	- Create and rehearse a detailed incident response plan.
1. Update Security Documentation:
	- Ensure all security documentation is up-to-date and comprehensive.
1. Conduct Staff Training:
	- Regularly train staff on new security threats and response techniques.

> :memo: **Conclusion:**

![Security Engineer After fixing the issue](smartmockups_lx84b4vq.jpg)
<small>_On-call Security Engineer After Fixing The Issue_</small>

In the face of adversity, our team rallied to defeat the hackers and restore our fortress. With fortified defenses and renewed vigilance, we stand ready to repel any future attacks. Onward and upward! 🚀
