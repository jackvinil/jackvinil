import os
import time
import random
from instagrapi import Client
from instagrapi.exceptions import LoginRequired

class InstagramScraper:
    def __init__(self, session_file="session.json"):
        self.cl = Client()
        self.session_file = session_file
        self.is_logged_in = False

    def login(self, username, password, verification_code=None):
        try:
            if os.path.exists(self.session_file) and not verification_code:
                self.cl.load_settings(self.session_file)
                try:
                    self.cl.login(username, password)
                    self.cl.get_timeline_feed()
                    self.is_logged_in = True
                    return True, "Login realizado com sucesso."
                except LoginRequired:
                    pass # Continue to normal login

            if verification_code:
                # Use the code provided by the user
                self.cl.login(username, password, verification_code=verification_code)
            else:
                # Attempt login normally
                self.cl.login(username, password)

            self.cl.dump_settings(self.session_file)
            self.is_logged_in = True
            return True, "Login realizado com sucesso."
        except Exception as e:
            err_msg = str(e).lower()
            if "two-factor" in err_msg or "verification_code" in err_msg:
                return "2FA", "Autenticação de dois fatores necessária."
            return False, str(e)

    def get_user_details(self, user_id):
        """
        Get detailed information about a user
        """
        try:
            # Adding a small delay to avoid rate limiting
            time.sleep(random.uniform(2, 5))
            user_info = self.cl.user_info(user_id)
            return user_info.dict()
        except Exception as e:
            print(f"Erro ao obter detalhes do usuário {user_id}: {e}")
            return None

    def map_user_data(self, data):
        """
        Map instagrapi user data to the requested CSV fields
        """
        # Help mapping friendship status
        friendship = data.get("friendship_status") or {}
        if not isinstance(friendship, dict):
            try:
                friendship = friendship.dict()
            except:
                friendship = {}

        # Mapping according to user request
        mapped = {
            "Username": data.get("username"),
            "Telefone 1": data.get("contact_phone_number"),
            "Nome completo": data.get("full_name"),
            "Tipo de conta": data.get("account_type"),
            "Biografia": data.get("biography"),
            "Categoria": data.get("category_name"),
            "Email": data.get("public_email"),
            "Telefone 3": data.get("whatsapp_number"),
            "Se é conta Privada": data.get("is_private"),
            "Se é perfil Verlicado": data.get("is_verified"),
            "Foto de perfil": data.get("profile_pic_url"),
            "Biografia Com Entidades": data.get("biography_with_entities"),
            "Nome da Cidade": data.get("city_name"),
            "Link Externo": data.get("external_url"),
            "Tradução Bio": data.get("biography_translation"),
            "URL Da Foto de Perfil": data.get("profile_pic_url_hd"),
            "Se é Comercial": data.get("is_business"),
            "Codigo Telefone 2": data.get("public_phone_country_code"),
            "CEP": data.get("zip"),
            "Endereco da rua": data.get("address_street"),
            "Método de contato Empresarial": data.get("business_contact_method"),
            "Id Cidade": data.get("city_id"),
            "Link Externo Luna": data.get("external_lynx_url"),
            "Número de Seguidores": data.get("follower_count"),
            "Numero Seguindo": data.get("following_count"),
            "Numero Tag Segundo": data.get("usertags_count"),
            "Status de Amicade Seguido": friendship.get("following"),
            "Status de Amizade Seguindo": friendship.get("followed_by"),
            "Numero de GeoMidia": data.get("geo_media_count"),
            "Versões da Foto de perfil": data.get("hd_profile_pic_versions"),
            "Uri Da Foto de Peril Anterior": data.get("profile_pic_id"),
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "Numero de Midias": data.get("media_count"),
            "ID da Pagina": data.get("page_id"),
            "ID da pagina pra Nova": data.get("page_id_for_new_persona"),
            "Nome da Pagina": data.get("page_name"),
        }

        # Critical Fix: Convert Pydantic objects (like HttpUrl) to strings
        # and lists/dicts to strings to avoid JSON serialization errors
        for key, value in mapped.items():
            if value is not None and not isinstance(value, (str, int, float, bool)):
                mapped[key] = str(value)

        return mapped
