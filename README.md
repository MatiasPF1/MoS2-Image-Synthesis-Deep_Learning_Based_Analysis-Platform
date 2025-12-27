# First Functional Version
- Work For The Advanced Quantumn Materials Lab, it aims to facilitate and have a general hub of the following:<br>
             1. **Generate Personalized XYZ and Params Files of MoS2:**<br>
                Creates atomic structure files (.xyz) and simulation parameters (.param) for MoS2 with customizable defects.<br>
                
                **XYZ File Format Example:**
                ```
                MoS2_incostem_10_17_1_Created_at_2024_12_26_15_30_45
                31.5000 54.5660 1.0000
                42 0.000000 0.000000 1.797500 1 0.08
                16 1.575000 3.030889 0.000000 1 0.08
                16 1.575000 3.030889 3.595000 1 0.08
                42 1.575000 9.092667 1.797500 1 0.08
                16 3.150000 12.123556 0.000000 1 0.08
                16 3.150000 12.123556 3.595000 1 0.08
                ...
                -1
                ```
                Format: `AtomicNumber X Y Z Occupancy DebyeWaller`
                - Generates pristine structures and defect label maps (metal dopants, vacancies, chalcogen substitutions)
                - Supports various defect types: single/double vacancies, substitutional dopants
                
                **Params File Format Example:**
                ```
                MoS2_incostem_10_17_1_0.xyz
                1 1 1
                ImageMoS2_incostem_10_17_1_0.tif
                512 512
                300 -0.003 0.0 -50 21.4
                70 200
                END
                0.45
                30
                y
                12.5 1e-6
                ```
                Parameters include: voltage (kV), spherical aberration (Cs3, Cs5), defocus (nm), aperture (mrad), ADF detector angles, source size (Å), defocus spread (Å), probe current (pA), dwell time (s)<br>
             
             3. **Post-processing of simulated STEM images:**<br>
                This module applies realistic noise profiles to synthetic STEM images to better simulate experimental conditions. The post-processing includes Gaussian noise, Poisson noise, and other imaging artifacts to enhance the realism of training data for machine learning models.<br>
             
*Note: Images for the model architecture and sample outputs will be added to the GitHub repository.*

# Workflow of the APP(Most current Version)
<img width="1241" height="954" alt="Mos2 drawio" src="https://github.com/user-attachments/assets/0c25ec6f-2f02-4597-ae9d-7f86f26030cb" />


# Worflow of the Folders 
<img width="1327" height="682" alt="FolderWorkflow" src="https://github.com/user-attachments/assets/84d53cb8-09fe-4468-9ccf-76798e2f3761" />
