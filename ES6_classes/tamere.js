function demoPortee() {
    // Portée de fonction
    var porteeDeFunction = "Je suis disponible dans toute la fonction";
    
    if (true) {
      // Portée de bloc
      let porteeDeBloc = "Je suis seulement disponible dans ce bloc";
      const aussiEnPorteeDeBloc = "Je suis aussi limité à ce bloc";
      
      console.log(porteeDeFunction);      // Fonctionne
      console.log(porteeDeBloc);          // Fonctionne
      console.log(aussiEnPorteeDeBloc);   // Fonctionne
    }
    
    console.log(porteeDeFunction);        // Fonctionne
    console.log(porteeDeBloc);            // Erreur de référence - non définie
    console.log(aussiEnPorteeDeBloc);     // Erreur de référence - non définie
  }

  