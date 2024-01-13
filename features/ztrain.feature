Feature: Tester Ztrain
  En tant qu'utilisateur
  Je veux utiliser les fonctionnalités du site
  Pour pouvoir acheter des produits, consulter mon profil et modifier mes données

  Scenario: Je m'inscris
    Given J'ouvre le formulaire d inscription
    When Je rentre les données d inscription
    Then J'appuie sur le bouton d inscription

  Scenario: Je me connecte
    Given J'ouvre le formulaire de connexion
    When Je rentre mes données de connexion
    Then J'appuie sur le bouton de connexion

  Scenario: Je cherche des produits par tags
    Given J'ouvre le sélecteur de tags
    When Je choisi le tag des produits
    Then Je navigue vers les éléments afficher par le tag

  Scenario: Je cherche des produits par des noms
    Given J'ouvre le barre de recherche
    When Je choisi le nom du produit
    Then Je navigue vers les éléments afficher par le nom

  Scenario: J'ajoute un produit au panier
    Given J'ouvre la barre de recherche pour le panier
    When Je choisi le nom du produit pour le panier
    When J'ouvre le produit sélectionné
    When Je sélectionne des informations
    Then J'ajoute au panier le produit

    Scenario: J'achète un produit
      Given J'ouvre le panier
      When J'ouvre la fenêtre d'achat
      When Je rentre les informations d'achat
      Then Je clique sur le bouton d'achat

    Scenario: Je modifie les informations du compte
      Given J'ouvre la page profile pour modifier mes informations de compte
      When Je remplis le formulaire d'informations
      Then J'appuie sur le bouton de modification

    Scenario: Je met à jour mon mot de passe
      Given J'ouvre la page profile pour modifier mon mot de passe
      When Je remplis le formulaire d'informations pour mon mot de passe
      When Je clique sur le bouton de modification
      When J'attend la notification m'informant de la réussite ou non
      Then Je réitère l'opération pour garder le mot de passe de base

    Scenario: Je réinitialise mon mot de passe
      Given J'ouvre la page de réinitialisation
      When Je remplis le formulaire de réinitialisation
      Then Je clique sur le bouton de réinitialisation de mot de passe

    Scenario: Je me déconnecte
      Given J'ouvre la page home
      Then Je clique sur le bouton de déconnexion
