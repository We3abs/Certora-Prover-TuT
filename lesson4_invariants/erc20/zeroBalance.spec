/*Checking if balance(0) have a value of 0
*ERC20 spec- invariant
*/
methods {
    // envfree functions 
    function totalSupply() external returns uint256 envfree;
    function balanceOf(address) external returns uint256 envfree;
    function allowance(address,address) external returns uint256 envfree;
}


// @title Checks that `transferFrom()`  decreases allowance of `e.msg.sender`
rule integrityOfTransferFrom(address sender, address recipient, uint256 amount) {
    env e;
    uint256 allowanceBefore = allowance(sender, e.msg.sender);
    require sender != recipient;
    require amount != 0;


    transferFrom(e, sender, recipient, amount);
    uint256 allowanceAfter = allowance(sender, e.msg.sender);



    
    assert (
        allowanceBefore > allowanceAfter
        ),
        "allowance must decrease after using the allowance to pay on behalf of somebody else";
}
invariant zeroHasNoBalance()
    balanceOf(0) == 0;