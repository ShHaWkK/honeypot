# Honeypot


## Structure du projet
- `scripts/`: Contient les scripts Shell pour démarrer et arrêter le honeypot.
- `src/`: Contient les scripts Python principaux.
- `logs/`: Contient les fichiers de log.
- `config/`: Contient les fichiers de configuration.

## PréRequis 
Pour utiliser la commande **ssh** sur Windows, vous devez installer OpenSSH. **Suivez ces étapes** :
 - Ouvrir les paramètres de Windows :
   - Allez dans Paramètres > Applications > **Fonctionnalités facultatives**.
  - Ajouter une fonctionnalité :
  - Recherchez OpenSSH Client et cliquez sur Installer.
## Utilisation
### Démarrer le Honeypot

```sh
cd scripts
./start_honeypot.sh
```

### Arrêter le Honeypot 

```sh 
cd scripts
./stop_honeypots.sh
```
