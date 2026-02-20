class Solution:
	def numUniqueEmails(self, emails: list[str]) -> int:
		if not emails:
			return 0

		unique_emails = set()

		for email in emails:
			local, domain = self.split_email(email)

			if self.is_quoted(local):
				local_content = local[1:-1]
				normalized_local = local_content

			else:
				local = local.split('+')[0]
				normalized_local = local.replace('.','')

			normalized_email = normalized_local + '@' + domain

			unique_emails.add(normalized_email)

		return len(unique_emails)

	def split_email(self, email: str) -> str:
		in_quotes = False
		escape = False
		for i, char in enumerate(email):
			if escape:
				escape = False
				continue
			if char == '\\':
				escape = True
				continue
			if char == '"':
				in_quotes = not in_quotes
				continue
			if char == '@' and not in_quotes:
				return email[:i], email[i+1:]
		# 引用符で囲まれていない '@' が存在しない場合
		return email, ""


	"""

	ローカル部分が引用符で囲まれているかどうかを判定する関数

	"""

	def is_quoted(self, local: str) -> bool:
		return len(local) >= 2 and local.startswith('"') and local.endswith('"')


#################################

	正規表現 version

#################################

class Solution:
	def numUniqueEmails(self, emails: list[str]) -> int:
		unique_address_set = set()
		for address in emails:
			local, domain = address.split('@')
			plus_ignored_local = re.sub(r'\+.*', '', local)
			dot_removed_local = re.sub(r'\.', '', plus_ignored_local)
			unique_address_set.add(f"{dot_removed_local}@{domain}")

		return len(unique_address_set)

##################################

	さらに高速化

##################################

class Solution:
	def numUniqueEmails(self, emails: list[str]) -> int:
		unique_emails = set()

		for address in emails:
			local_name, domain_name = address.split("@", 1)
			local_name = local_name.split("+", 1)[0].replace(".", "")
			unique_emails.add(f"{local_name}@{domain_name}")

		return len(unique_emails)
