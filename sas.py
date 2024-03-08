import os

html = """
			<div class="nav-item">
				<a href="wiki/City/City.html">City</a>
					<div class="dropdown">
						<a href="wiki/City/Basic_Info.html">Basic Info</a>
						<div class="dropdown-item">
							<a href="wiki/City/Districts/Districts.html">Districts</a>
							<div class="dropdown-sub">
								<a href="wiki/City/Districts/Citizen_Quarter.html">Citizen's Quarter</a>
								<a href="wiki/City/Districts/Studenski_Kvartal.html">Studenski Kvartal</a>
								<a href="wiki/City/Districts/Heliosentrum.html">Heliosentrum</a>
            				    <a href="wiki/City/Districts/Dreiländereck.html">Dreiländereck</a>
         				       <a href="wiki/City/Districts/Hranicne_Dol.html">Hranicne Dol</a>
        				        <a href="wiki/City/Districts/Novi_Park.html">Novi Park</a>
     				       </div>
   				     </div>
   				     <a href="wiki/City/Metro.html">Metro</a>
   				 </div>
			</div>
			<div class="nav-item">
  				<a href="wiki/Characters/Characters.html">Characters</a>
  				<div class="dropdown">
  				    <div class="dropdown-item">
   				        <a href="wiki/Characters/Esperes/Esperes.html">Esperes</a>
     				    <div class="dropdown-sub">
     				        <div class="dropdown-sub-item">
      				            <a href="/wiki/Characters/Esperes/Fifth_Levels/Fifth_Levels.html">Fifth Levels</a>
								<div class="dropdown-sub-sub">
                                    <a href="wiki/Characters/Esperes/Fifth_Levels/Jorn_Mann.html">Jorn Mann</a>
									<a href="wiki/Characters/Esperes/Fifth_Levels/Skylar_del_Marler.html">Skylar del Marler</a>
 									<a href="wiki/Characters/Esperes/Fifth_Levels/Luke_Kondrashov.html">Luke Kondrashov</a>
									<a href="wiki/Characters/Esperes/Fifth_Levels/Vreni_von_Nürchtag.html">Vreni von Nürchtag</a>
									<a href="wiki/Characters/Esperes/Fifth_Levels/Victoria_Le_British.html">Victoria Le British</a>
									<a href="wiki/Characters/Esperes/Fifth_Levels/Alma_Dresdner.html">Alma Dresdner</a>
								</div>
							</div>
							<div class="dropdown-sub-item">
								<a href="wiki/Characters/Esperes/Experimental/Experimental.html">Experimental</a>
								<div class="dropdown-sub-sub">
									<a href="wiki/Characters/Esperes/Experimental/Abigail_Watson.html">Abigail Watson</a>
								</div>
							</div>
							<div class="dropdown-sub-item">
								<a href="wiki/Characters/Esperes/Others/Others.html">Others</a>
								<div class="dropdown-sub-sub">
									<a href="wiki/Characters/Esperes/Others/Adrien_Fakras.html">Adrien Fakras</a>
									<a href="wiki/Characters/Esperes/Others/Mila_Petrovic.html">Mila Petrovic</a>
									<a href="wiki/Characters/Esperes/Others/Elizabeth.html">Elizabeth</a>
								</div>
							</div>
						</div>
					</div>
					<div class="dropdown-item">
						<a href="wiki/Characters/Scientists/Scientists.html">Scientists</a>
						<div class="dropdown-sub">
							<a href="wiki/Characters/Scientists/Governmental.html">Governmental</a>
							<a href="wiki/Characters/Scientists/Independent.html">Independent</a>
						</div>
					</div>
					<div class="dropdown-item">
						<a href="wiki/Characters/Zeros/Zeros.html">Zeros</a>
						<div class="dropdown-sub">
							<div class="dropdown-sub-item">
								<a href="wiki/Characters/Zeros/Ordinary_people/Ordinary_people.html">Ordinary people</a>
								<div class="dropdown-sub-sub">
									<a href="wiki/Characters/Zeros/Ordinary_people/Marshall_Townley.html">Marshall Townley</a>
								</div>
							</div>
							<a href="wiki/Characters/Zeros/Government.html">Government</a>
						</div>
					</div>
				</div>
			</div>
			<div class="nav-item">
			<a href="wiki/Science/Science.html">Science</a>
				<div class="dropdown">
					<div class="dropdown-item">
						<a href="wiki/Science/Projects/Projects.html">Projects</a>
						<div class="dropdown-sub">
							<a href="wiki/Science/Projects/The_Storm.html">The Storm</a>
							<a href="wiki/Science/Projects/The_Real_One_Around.html">The Real One Around</a>
						</div>
					</div>
					<a href="wiki/Science/Experiments.html">Experiments</a>
					<a href="wiki/Science/Labs.html">Labs</a>
				</div>
			</div>
			<div class="nav-item">
				<a href="wiki/Details/Details.html">Details</a>
				<div class="dropdown">
					<a href="wiki/Details/Organizations.html">Organizations</a>
					<a href="wiki/Details/Important_Events.html">Important Events</a>
				</div>
"""

# Extract all href paths
paths = [match.split('"')[1] for match in html.split('href=')[1:]]

# Convert paths to OS-specific format
paths = [os.path.join(*path.split('/')) for path in paths]

# Specify the paths to the template files
template_paths = {
    "city": "C:\\wiki\\City.html",  # Replace with the actual path to your city template
    "characters": "C:\\wiki\\Characters.html",  # And so on for the other templates
    "sciences": "C:\\wiki\\Sciences.html",
    "details": "C:\\wiki\\Details.html",
}

# Create directories and files
for path in paths:
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    
    # Choose the template file based on the directory
    for key in template_paths.keys():
        if key in directory:
            template_path = template_paths[key]
            break
    else:
        continue  # Skip if none of the keys are in the directory

    # Copy the template file
    if not os.path.exists(path):
        shutil.copy(template_path, path)