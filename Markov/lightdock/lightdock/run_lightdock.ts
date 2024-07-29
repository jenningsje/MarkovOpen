const { exec } = require('child_process');

//file paths to receptor and ligand
const path1 = './../../MarkovProprietary/pipelinestages/app/mount/input/prot1/*pdb'
const path2 = './../../MarkovProprietary/pipelinestages/app/mount/input/prot2/*pdb'

// execute analyze.py
function executeCommand(cmd) {
	exec(cmd, (error, stdout, stderr) => {
	if (error) {
	console.log(`error: ${error.message}`);
		return;
	}
	else if (stderr) {
		console.log(`stderr: ${stderr}`);
		return;
	}
	//console.log(`stdout: ${stdout}`);
	else {
		console.log(stdout);
	}
	});
};

// activate the conda environment
executeCommand('source venv/bin/activate')

// setup lightdock
executeCommand(`gd_setup.py ${path1} ${path2} --noh --now`)

// run lightdock
executeCommand('lgd_run.py -s template setup.json 100 -c 1 -l 0')