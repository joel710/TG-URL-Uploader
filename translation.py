class Translation(object):
    START_TEXT = """Hello,
Il s'agit d'un bot de téléchargement d'URL Telegram ! 
<b>Veuillez m'envoyer un lien URL de téléchargement direct, je peux télécharger sur un télégramme en tant que fichier/vidéo</b>

/aide pour plus de détails..
"""
    RENAME_403_ERR = "Pardon. Vous n'êtes pas autorisé à renommer ce fichier."
    ABS_TEXT = " S'il vous plaît ne soyez pas égoïste."
    UPGRADE_TEXT = "<b>👉 Créer son propre bot clone.. </b>  /help for Details"
    FORMAT_SELECTION = "Sélectionnez le format souhaité: <a href='{}'>file size might be approximate</a> \nSi vous souhaitez définir une vignette personnalisée, envoyez une photo avant ou rapidement après avoir appuyé sur l'un des boutons ci-dessous.\nYou can use /deletethumbnail pour supprimer la vignette générée automatiquement."
    SET_CUSTOM_USERNAME_PASSWORD = """Si vous souhaitez télécharger des vidéos premium, fournissez-les au format suivant:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "trying to download"
    UPLOAD_START = "trying to upload"
    RCHD_BOT_API_LIMIT = "taille supérieure à la taille maximale autorisée (50MB). Néanmoins, j'essaie de télécharger."
    RCHD_TG_API_LIMIT = "Téléchargé en {} seconds.\nTaille de fichier détectée: {}\nPardon. Mais, je ne peux pas télécharger de fichiers supérieurs à 1.5GB en raison des limitations de  l'API Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Veuillez m'évaluer si vous me trouvez utile. @jojo_dev"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Téléchargé en {} seconds. \n @jojo_dev \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "S'il vous plaît /mettre à niveau votre abonnement."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Taille de fichier détectée: {}.Les utilisateurs gratuits ne peuvent télécharger que: {}\nS'il vous plaît /mettre à niveau votre abonnement.\nSi vous pensez qu'il s'agit d'un bug, veuillez contacter <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Vignette vidéo/file personnalisée enregistrée. Cette image sera utilisée dans la vidéo/file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Vignette personnalisée effacée avec succès."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Média effacé avec succès."
    SAVED_RECVD_DOC_FILE = "Document téléchargé avec succès."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Aucune miniature personnalisée n'a été trouvée."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "Utilisateur <a href='tg://user?id={}'>{}</a> ajouté à {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: Free Cloned User
Expires on: 31/12/2022"""
    HELP_USER = """Je suis le bot URL Uploader ..
    
1. URL d'envoi (Lien|Nouveau nom avec extension).
2. Envoyer une miniature personnalisée (facultatif).
3. Sélectionnez le bouton.
   SVideo - Donner le fichier en vidéo avec des captures d'écran
   DFile  - Donner un fichier avec des captures d'écran
   Video  - Donner le fichier sous forme de vidéo sans captures d'écran
   DFile  - Donner un fichier sans captures d'écran

--------
@jojo_dev
"""
    REPLY_TO_DOC_GET_LINK = "Répondez à un média Telegram pour obtenir un lien de téléchargement direct à grande vitesse"
    REPLY_TO_DOC_FOR_C2V = "Répondre à un média Telegram pour convertir "
    REPLY_TO_DOC_FOR_SCSS = "Répondre à un média Telegram pour obtenir des captures d'écran"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Répondre à un média Telegram à / rename avec la prise en charge des vignettes personnalisées"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\nt"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Premier envoi /downloadmedia sur n'importe quel support afin qu'il puisse être téléchargé sur mon local. \nEnvoyer /storageinfo connaître le média actuellement téléchargé."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nEnvoyer  /clearffmpegmedia pour supprimer ce média, de mon espace de stockage.\nEnvoyer  /trim HH:MM:SS [HH:MM:SS] to cu[l]t une petite photo / video, des médias ci-dessus."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Un média enregistré existe déjà. Envoyez s'il vous plaît/storageinfo pour connaître les détails  des médias actuels ."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> supprimé de la base de données."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Répondre à un média Telegram (MKV), pour extraire les flux embarqués"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Réponse /generatecustomthumbnail à un album multimédia, pour générer une vignette personnalisée"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "L'album multimédia ne doit contenir que deux photos. Veuillez renvoyer l'album multimédia, puis réessayer, ou envoyez seulement deux photos dans un album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "Le format de l'URL est incorrect. assurez-vous que votre URL commence par soit http:// or https://. Vous pouvez définir un nom de fichier personnalisé à l'aide du lien de format | file_name.extension"
    ABUSIVE_USERS = "Vous n'êtes pas autorisé à utiliser ce bot. Si vous pensez qu'il s'agit d'une erreur, veuillez vérifier /me pour supprimer cette restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Envoyez d'abord un fichier compressé, puis répondez /unzip commande au fichier."
    EXTRACT_ZIP_INTRO_THREE = "Analyse du fichier reçu. ⚠️ Cela peut prendre un certain temps. S'il vous plaît soyez patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Pardon. Des erreurs se sont produites lors du traitement du fichier compressé. Veuillez tout vérifier à nouveau deux fois, et si le problème persiste, signalez-le à <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Sélectionnez file_name à télécharger parmi les options ci-dessous.
Vous pouvez utiliser /rename commande après réception du fichier pour le renommer avec la prise en charge des vignettes personnalisées."""
    CANCEL_STR = "Processus annulé"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh qui semble être une URL très lente. Puisque vous étiez en train de foutre en l'air ma maison, je ne suis pas d'humeur à télécharger ce fichier. En attendant, pourquoi n'essayez-vous pas ceci:==> https://shrtz.me/PtsVnf6 et obtenez-moi une URL rapide pour que je puisse télécharger sur Telegram, sans que je ralentisse pour les autres utilisateurs."
