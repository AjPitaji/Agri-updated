from supabase_py import create_client

# Initialize Supabase client
supabase_url = 'https://sdfsbfadqqhvjvbwwzxz.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNkZnNiZmFkcXFodmp2Ynd3enh6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMwNzIxODksImV4cCI6MjAxODY0ODE4OX0.bbQ096D3rpJ2Nk8_junkWs6OgyzaX6xOCFD_liY-yW0'
supabase = create_client(supabase_url, supabase_key)
