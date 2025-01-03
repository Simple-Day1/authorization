FROM python
WORKDIR /new_app
COPY app/application/commands/sign_in_account.py /new_app/sign_in.py
ENTRYPOINT ["python", "sign_in.py"]