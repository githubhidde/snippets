#!/bin/bash

# Check the url: https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/shell

# Simple, remove the spaces from the string, then return the resultant string.

var="$1"

echo ${var// /}

#    it "should print proper output" do
#      output = run_shell args: ['8 j 8   mBliB8g  imjB8B8  jl  B']
#      expect(output).to eq("8j8mBliB8gimjB8B8jlB")
#    end
# end

# describe "Solution for parameter '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'" do
#    it "should print proper output" do
#      output = run_shell args: ['8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd']
#      expect(output).to eq("88Bifk8hB8BB8BBBB888chl8BhBfd")
#    end
# end

# describe "Solution for parameter '8aaaaa dddd r     '" do
#    it "should print proper output" do
#      output = run_shell args: ['8aaaaa dddd r     ']
#      expect(output).to eq("8aaaaaddddr")
#    end
# end

# describe "Solution for parameter 'jfBm  gk lf8hg  88lbe8 '" do
#    it "should print proper output" do
#      output = run_shell args: ['jfBm  gk lf8hg  88lbe8 ']
#      expect(output).to eq("jfBmgklf8hg88lbe8")
#    end
# end

# describe "Solution for parameter '8j aam'" do
#    it "should print proper output" do
#      output = run_shell args: ['8j aam']
#      expect(output).to eq("8jaam")
#    end
# end

