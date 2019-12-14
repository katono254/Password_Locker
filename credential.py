import random
import string

class UserCredential:
    credentials_list = [] #empty array for the credential section.
    def __init__(self,media,email,p_code,u_name):
        """
        __init__ method that helps us define properties for our objects.

        Args:
        media: New credential media.
        email : New credential email.
        p_code: New credential password/passcode.
        u_name : New credential username.
        """
        self.media = media
        self.email = email
        self.p_code = p_code
        self.u_name = u_name


    def save_credential(self):
        """
		this function is for saving the different credentials of our users.		
		"""
        UserCredential.credentials_list.append(self)
        UserCredential.generate_password()
        @classmethod
        def generate_password(cls,stringLength=8)
        """
        this is the method to help users generate passwords for them
        """

        """
        Generate a random string of letters and digits for password
        """
        

		
