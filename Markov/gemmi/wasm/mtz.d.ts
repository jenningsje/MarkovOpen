// interface for mtz.js that can be built with "make mtz.js"

export interface UnitCell {
  a: number;
  b: number;
  c: number;
  alpha: number;
  beta: number;
  gamma: number;
  delete(): void;
}

export interface Mtz {
  readonly cell: UnitCell;
  readonly nx: number;
  readonly ny: number;
  readonly nz: number;
  readonly rmsd: number;
  readonly last_error: string;
  read(_0: number, _1: number): boolean;
  calculate_map(_0: boolean): any;
  calculate_map_from_labels(_0: string, _1: string): any;
  delete(): void;
}

export interface Module {
  readonly HEAPU8: Uint8Array;
  readMtz(mtz_buf: string|ArrayBuffer): Mtz;
}
