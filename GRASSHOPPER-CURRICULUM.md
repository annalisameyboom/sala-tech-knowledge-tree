# Grasshopper Curriculum

The knowledge spine for learning Grasshopper, independent of any interface. Eight chapters in learning order; each section says what it teaches and which collected resources cover it. Sections marked **[gap]** have no dedicated resource yet and are candidates for the next recordings.

Resource sources:
- **DES 212** = Xun Liu's course tutorials (genenv.github.io/des212-2026)
- **DM1** = ARCH 515 Design Media I session (Notion)
- **Medium** = "Intro to Grasshopper" written series
- **DC** = Daniel Christey video series (TA-recommended)
- **Video** = other TA-recommended videos

---

## Chapter 1: First Contact

- **1.1 What Grasshopper is.** Visual programming, parametric thinking, and the relationship to Rhino.
  - Medium: Getting started with Grasshopper (https://medium.com/intro-to-grasshopper/getting-started-with-grasshopper-c6d9e66a4638)
  - DC: Intro to Grasshopper (https://youtu.be/Il2OjDH9eF8)
- **1.2 Interface and canvas.** Layout, navigation, finding components.
  - Medium: Navigating the canvas (https://medium.com/intro-to-grasshopper/navigating-the-canvas-ab9ab46d8f8e)
  - DES 212: Hello, Grasshopper, part 1 (https://www.youtube.com/watch?v=0HoOkWAA0l8)
- **1.3 Anatomy of a definition.** Components, inputs and outputs, wires, data flow direction.
  - Medium: Anatomy of a definition (https://medium.com/intro-to-grasshopper/anatomy-of-a-definition-1dc644e13212)
- **1.4 Sliders, panels, baking.** Parameters as controls, inspecting data, getting geometry back into Rhino, .gh and .3dm file sync.
  - DES 212: Hello, Grasshopper, components file (https://genenv.github.io/des212-2026/pages/tutorial-1-1.html)
- **1.5 Exercise: first definition.**
  - Medium: Exercise, Hello Grasshopper (https://medium.com/intro-to-grasshopper/exercise-hello-grasshopper-c3cd53dd19d5?sk=86b6b3a70fa990730e02552e56db38c9)
  - DES 212: Hello, Grasshopper, practice videos 1 to 3 (https://www.youtube.com/watch?v=GEVUv-G8ESA, https://www.youtube.com/watch?v=LvlUjEsT-h0, https://www.youtube.com/watch?v=SNZH_bDYiNw)
  - DM1: Grasshopper Basic + Topography (https://app.notion.com/p/3ec3b7ec1ca14ed7aa7dbd44b7adaa2d)

## Chapter 2: Data Basics, Lists

- **2.1 Data types and domains.** Numbers, points, geometry as data; intervals. **[gap: no dedicated resource; touched inside 1.x and 3.x videos]**
- **2.2 Making and reading lists.** Panels, param viewers, list length and indices.
  - Medium: Working with lists (https://medium.com/intro-to-grasshopper/working-with-lists-e9ce209f0bd5)
  - DC: Intro to lists (https://youtu.be/Am8wLTam_cc)
- **2.3 List operations.** Item, shift, cull, sort, weave, combining lists.
  - DC: Editing and combining lists (https://youtu.be/sBDwmPyCZ6g)
- **2.4 Generating numbers.** Series, range, and why the difference matters. **[gap: covered in passing inside 2.2 resources; no standalone]**
- **2.5 Exercise: Parametric Tower, part 1.**
  - Medium: Exercise, Parametric Tower part 1 (https://medium.com/intro-to-grasshopper/exercise-parametric-tower-part-1-bdbad26bc6ca)
  - Video: Parametric Tower (https://youtu.be/C_tM_v9Zdag)

## Chapter 3: Geometry Fundamentals

- **3.1 Points and vectors.** Position versus direction; vector math for designers.
  - DES 212: Vectors in Grasshopper (https://genenv.github.io/des212-2026/pages/vectors-in-grasshopper.html)
  - Video: Basics of geometry (https://youtu.be/3ef_M3cw-2w)
- **3.2 Curves.** Creation, divide, evaluate, curve parameters.
  - DC: Curve functionality (https://youtu.be/JrDduldZ2tM)
- **3.3 Planes and coordinate systems.** The second secret ingredient; local frames for placement and orientation.
  - DES 212: Planes in Grasshopper (https://genenv.github.io/des212-2026/pages/planes-in-grasshopper.html)
- **3.4 Surfaces and UV space.** Surface creation, evaluation, isocurves. **[gap: partially inside 3.1 geometry video and 6.x; no standalone]**
- **3.5 Transformations.** Move, rotate, scale, orient, morph, built on vectors and planes.
  - DES 212: Transformations in Grasshopper (https://genenv.github.io/des212-2026/pages/transformations-in-grasshopper.html)
  - DC: Transforming geometry (https://youtu.be/XWNzRBorXDk)

## Chapter 4: Data Trees

- **4.1 Why trees exist.** Paths, branches, and where 90 percent of Grasshopper errors come from.
  - Medium: Working with data trees (https://medium.com/intro-to-grasshopper/working-with-datatrees-179be560f086?sk=0c0755e369f9337e8c882874c20ff95b)
  - DC: Intro to data structures (https://youtu.be/XIV0uQ6ZOjI)
  - DES 212: data structure video series (https://www.youtube.com/playlist?list=PL5TCFBlAxkAgTdBm-P-7DJu8MkG_B0gUa)
- **4.2 Graft, flatten, simplify.** With intent, not as superstition.
  - Covered inside 4.1 resources; DES 212 Attractors + Data Structure (https://genenv.github.io/des212-2026/pages/tutorial-1-2.html)
- **4.3 Tree matching.** How components pair branches; longest list versus cross reference.
  - DC: Data structures II (https://youtu.be/QE68l1Fp7-c)
- **4.4 Path Mapper and advanced operations.**
  - Video: Using the Path Mapper (https://youtu.be/Tlme9tkpYHo)
- **4.5 Exercise: Parametric Tower, part 2.**
  - Medium: Exercise, Parametric Tower part 2 (https://medium.com/intro-to-grasshopper/exercise-parametric-tower-part-2-2052c179c6e1)

## Chapter 5: Control and Pattern

- **5.1 Attractors.** Point, curve, and multiple attractors; distance as a design driver.
  - DES 212: Grasshopper Attractors, Keio paving (https://www.youtube.com/watch?v=8O6ZdzTGVZw)
  - Video: Attractor points intro + example (https://youtu.be/Vyst-H_muuI, https://youtu.be/r_1FSc6k7-8)
- **5.2 Remapping numbers.** Graph Mapper, remap domains, easing control.
  - Video: Using the Graph Mapper (https://youtu.be/3FA_1sL6J0w)
- **5.3 Grids, Voronoi, and subdivision patterns.**
  - DES 212: stochastic systems and 3D Voronoi (https://www.youtube.com/watch?v=Nc1eSjw2elg)
  - Video: Voronoi (https://youtu.be/dt4Gpaw4tEM)
- **5.4 Randomness and seeds.** Jitter, random, repeatability. **[gap: touched inside 5.3; no standalone]**

## Chapter 6: Surfaces and Structures

- **6.1 Surface subdivision.** Isotrim, divide surface, paneling logic. **[gap: taught inside 6.2 resource; no standalone]**
- **6.2 Structures on surfaces.** Subdividing a surface to place a structural system.
  - Video: Structures on surfaces (https://youtu.be/pbrlZsjI58c)
- **6.3 Project exercises.**
  - Video: Parametric bench (https://youtu.be/03R1vXfIZF4)
  - Video: Roof space frame (https://youtu.be/qNJ9FWrl-Wk)

## Chapter 7: From Definition to Deliverable

- **7.1 Baking, layers, attributes.** Getting organized geometry out. **[gap: touched in 1.4; no standalone]**
- **7.2 Definition hygiene.** Groups, annotation, clusters; definitions others can read.
  - DES 212: organizing the Grasshopper workspace (https://www.youtube.com/watch?v=dAHP0M2GgCs)
- **7.3 Plugins.** Finding, installing, and managing plugins.
  - Video: Importing plugins (https://youtu.be/74P-7YME1hM)
  - DES 212: plugin installation guide (https://genenv.github.io/des212-2026/pages/grasshopper-plugin-installation.html)

## Chapter 8: Applied Workflows

- **8.1 Terrain and topography.** Terrain from contours and data.
  - DM1: Grasshopper Basic + Topography (https://app.notion.com/p/3ec3b7ec1ca14ed7aa7dbd44b7adaa2d)
- **8.2 Site data.** OSM to 3D site model with Caribou; shapefiles and spreadsheets.
  - DES 212: Spatial Data (https://genenv.github.io/des212-2026/pages/tutorial-3-1.html)
- **8.3 Environmental simulation.** Ladybug: EPW data, sun, radiation, wind.
  - DES 212: Environmental Simulation (https://genenv.github.io/des212-2026/pages/tutorial-3-2.html)
- **8.4 Optimization.** Galapagos: genome, fitness, penalty; beyond to multi-objective.
  - DES 212: Evolutionary Solvers (https://genenv.github.io/des212-2026/pages/tutorial-3-3.html)
- **8.5 Robotic fabrication.** Toolpaths from Grasshopper with the Robots plugin.
  - DES 212: Robotic Fabrication with the UR30 (https://genenv.github.io/des212-2026/pages/tutorial-2-3.html)

---

## Notes on the structure

- Chapters 1, 2, 4 are the non-negotiable core in that order; 3 can interleave with 2; 5 through 7 can be taken in any order after 4; chapter 8 sections are independent electives, each assuming chapters 1 to 4.
- Every section intentionally allows multiple parallel resources (written, video, SALA-taught) covering the same concept, so students choose their format.
- Seven **[gap]** sections currently lack a dedicated resource: 2.1 data types, 2.4 number generation, 3.4 surfaces and UV, 5.4 randomness, 6.1 subdivision basics, 7.1 baking and attributes. These are short topics; most would be 10 to 15 minute recordings and are natural first assignments for TA or faculty contributors.
