import dns.resolver
import logging

logger = logging.getLogger(__name__)

def check(host, domain):
    result = False
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [host]
    try:
        result = resolver.query(domain)
    except Exception as e:
        logger.error(e)
        result = False
    return result
