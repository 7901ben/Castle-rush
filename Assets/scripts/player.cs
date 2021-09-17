using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player : MonoBehaviour
{   //handle to player animation
    private playerAnimation _playerAnim;
    // Start is called before the first frame update
    // get handle to rigid body 
    private Rigidbody2D _rigid;
    [SerializeField] private float _jumpForce = 50.0f;
    [SerializeField] private bool _grounded = false;
   [SerializeField] private LayerMask _groundLayer;
    private bool resetJumpNeeded = false;
    private SpriteRenderer _playerSprite;
    float move;
    void Start()
    {
        //assign handle of rigid body 
        _rigid = GetComponent<Rigidbody2D>();
        _playerAnim = GetComponent<playerAnimation>();
        _playerSprite = GetComponentInChildren<SpriteRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        //input for left or right 
        movement();
        _rigid.velocity = new Vector2(move * 2.5f, _rigid.velocity.y);
        //raycast
        checkGrounded();
        if(Input.GetMouseButtonDown(0) && _grounded == true)
        {
            _playerAnim.Attack();

        }

    }

    void movement()
    {
         move = Input.GetAxisRaw("Horizontal");
        flip();
        _playerAnim.Jump(true);
        //use rigidbody components to move character 
         if (Input.GetKeyDown(KeyCode.Space) && _grounded == true)
        {
            //jump
            _rigid.velocity = new Vector2(_rigid.velocity.x, _jumpForce);
            _grounded = false;
            // resetJumpNeeded = true;
            //StartCoroutine(resetJumpRoutine());
            //resetJumpNeeded = false;
            //_playerAnim.Jump(true);
            }
        _playerAnim.Move(move);
    }

    void checkGrounded()
    {
        RaycastHit2D hitInfo = Physics2D.Raycast(transform.position + new Vector3(-1.75f, 0.5f, 0f), Vector2.down * 0.5f, 0.5f, _groundLayer.value);
        Debug.DrawRay(transform.position + new Vector3(-1.75f, 0.5f, 0f), Vector2.down * 0.5f, Color.green);
        if (hitInfo.collider != null)
        {
            Debug.Log("Hit:" + hitInfo.collider.name);
            //  if (resetJumpNeeded = false)
            _playerAnim.Jump(false);
            _grounded = true;

        }
        
    }

    void flip()
    {
        //sprite flip
        if (move > 0)
        {
            _playerSprite.flipX = false;
        }
        else if (move < 0)
        {
            _playerSprite.flipX = true;
        }
    }

    IEnumerator resetJumpRoutine()
    {
        yield return new WaitForSeconds(0.1f);
        resetJumpNeeded = false;
    }
}

 