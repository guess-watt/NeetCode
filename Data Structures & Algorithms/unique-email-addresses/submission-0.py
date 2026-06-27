class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local,domain = email.split('@')
            if "+" in local:
                local = local[:local.index("+")]
            if "." in local:
                local = local.replace(".","")
            result_mail = local + "@" + domain
            result.add(result_mail)
        return len(result)
