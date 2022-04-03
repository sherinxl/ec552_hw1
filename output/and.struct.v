module and_gate (input a, b, output out);

	wire \$n5_0;
	wire \$n4_0;

	not (\$n4_0, a);
	not (\$n5_0, b);
	nor (out, \$n5_0, \$n4_0);

endmodule
