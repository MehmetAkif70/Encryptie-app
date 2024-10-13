# Encryptie-app

## Inleiding

In de wereld van cryptografie zijn er twee hoofdcategorieën van encryptie: symmetrische en asymmetrische encryptie.

### Symmetrische Encryptie
Symmetrische encryptie is een cryptografisch proces waarbij dezelfde sleutel wordt gebruikt voor zowel de encryptie als de decryptie van gegevens. Dit betekent dat de verzender en ontvanger allebei dezelfde geheime sleutel moeten delen om de gegevens te versleutelen en te ontsleutelen. Het grootste voordeel van symmetrische encryptie is de snelheid, omdat het een relatief eenvoudig proces is. Het nadeel is echter dat de geheime sleutel op een veilige manier gedeeld moet worden tussen de betrokken partijen.

### Asymmetrische Encryptie
In asymmetrische encryptie worden twee verschillende sleutels gebruikt: een openbare sleutel voor de encryptie en een privé-sleutel voor de decryptie. Dit betekent dat je een bericht kunt versleutelen met de openbare sleutel van de ontvanger, en alleen de ontvanger kan het bericht ontsleutelen met zijn privé-sleutel. Het voordeel hiervan is dat er geen sleuteluitwisseling nodig is, maar het nadeel is dat asymmetrische encryptie veel langzamer is dan symmetrische encryptie.

### Keuze van Encryptie Methode
Voor deze applicatie maken we gebruik van **symmetrische encryptie**, specifiek de **Fernet**-methode, onderdeel van de `cryptography`-library. Fernet biedt sterke encryptie met behulp van AES (Advanced Encryption Standard) in combinatie met een HMAC (Hash-based Message Authentication Code) om ervoor te zorgen dat de gegevens zowel veilig als authentiek zijn.

---

## Hoe de App Werkt

Deze app stelt de gebruiker in staat om tekst te versleutelen en te ontsleutelen met behulp van symmetrische encryptie. De app gebruikt de `cryptography`-library in Python en implementeert de **Fernet**-encryptie. Hieronder wordt uitgelegd hoe de verschillende onderdelen van de app werken.

### 1. Sleutelgeneratie
Bij de eerste keer dat de app wordt uitgevoerd, genereert het programma een willekeurige symmetrische sleutel met behulp van de `Fernet.generate_key()`-functie. Deze sleutel wordt opgeslagen in een bestand genaamd `secret.key`. Als de sleutel al bestaat, wordt deze geladen vanuit het bestand. De sleutel moet veilig worden bewaard, omdat deze nodig is voor zowel encryptie als decryptie.

### 2. Encryptie
Gebruikers kunnen een bericht invoeren dat ze willen versleutelen. De functie `encrypt_message()` gebruikt de geladen sleutel om het bericht te versleutelen met Fernet. De versleutelde tekst wordt weergegeven in de terminal.

### 3. Decryptie
Gebruikers kunnen ook een eerder versleuteld bericht invoeren om het te ontsleutelen. De functie `decrypt_message()` gebruikt de eerder gegenereerde sleutel om het bericht te ontsleutelen. De oorspronkelijke tekst wordt weergegeven als de juiste sleutel is gebruikt. Als de verkeerde sleutel is ingevoerd, zal de decryptie mislukken.

---

## Installatie en Uitvoering

Volg de onderstaande stappen om de app op je lokale machine te draaien:

1. **Vereisten installeren:**
   Zorg ervoor dat je Python hebt geïnstalleerd op je systeem en installeer de `cryptography`-library:
   
   ```bash
   pip install cryptography
